import sys
import re
from stringSearch import findLineNumWithComments, string2list
from getUnitGeom import getUnitGeom
from getArrayData import getArrayData

def fixUnitsWithArrays(new_input,unitGeom=0,arrayData=0):
 
  print 'Running fixUnitsWithArrays'

  if unitGeom == 0:
    unitGeom = getUnitGeom(new_input)
  if arrayData == 0:
    arrayData = getArrayData(new_input)

  start_geom = findLineNumWithComments(new_input,'read geom')
  end_geom = findLineNumWithComments(new_input,'end geom', start_index=start_geom)

  """ Start by calculating the x and y dimensions of the array. 
        A) Find nux and nuy
        B) Make a list of units which span the x and y dimensions of the array
        C) Find the size of each of these units
          1)  Find which region is the boundary for the unit
          2) Find the dimension of that region
        D) Sum up the unit dimensions to ge the array dimension """

  # Remove any redundant spaces to make parsing simpler
  for line_num in range(start_geom,end_geom):
    new_input[line_num] = re.sub('[ ]+',' ', new_input[line_num])

  for array_num in arrayData.keys():
    units_x = []
    units_y = []
    nux = arrayData[array_num]['nux']
    nuy = arrayData[array_num]['nuy']
    for position in range(nux):
      units_x.append(arrayData[array_num]['unitGivenLocation'][position])
    # this units_y part will only work for a cuboidal array
    for position in range(0,nux*nuy,nux):
      units_y.append(arrayData[array_num]['unitGivenLocation'][position])
    unit_size = []
    array_size_x = 0.0
    for unit in units_x:
      boundary_region = unitGeom[unit]['boundaryRegion']
      unit_size = abs(unitGeom[unit][boundary_region]['dimension']['x+']) + abs(unitGeom[unit][boundary_region]['dimension']['x-'])
      array_size_x = array_size_x + unit_size
#    print array_size_x
    unit_size = []
    array_size_y = 0.0
    for unit in units_y:
      boundary_region = unitGeom[unit]['boundaryRegion']
      unit_size = abs(unitGeom[unit][boundary_region]['dimension']['y+']) + abs(unitGeom[unit][boundary_region]['dimension']['y-'])
      array_size_y = array_size_y + unit_size
#    print array_size_y

    """ Now for each array:
        E) go to the unit where the array is described
        F) Read the array definition
        G) Determine which surface is being filled in the array
        H) If this surface is larger than array_size_x and array_size_y
          1) Make a new surface that has dimensions array_size_x and array_size_y
            a) If array_size_x == array_size_y
              i) Adjust the x+ and x- equally to get the correct size surface
              ii) Adjust the y+ and y- equally to get the correct size surface
            b) If array_size_x != array_size_y
              i) Adjust the x+ dimension to get the correct size surface
              ii) Adjust the y- dimension to get the correct size surface
          2) Change the array definition such that this new_surface is the one being filled
          3) Add "-" + new_suface_number to the media describing the old surface number
    """
    # This is the unit where the array is used
    unit = arrayData[array_num]['locatedInUnit']
#    print 'The Unit we want is ', unit
    # Find the start and end of the desciption for the unit
    unit_search = re.compile(r'unit\s+(\d+)')
    search_line = start_geom
    for line_num in range(start_geom, end_geom):
      tmp_line_num = findLineNumWithComments(new_input,'unit',start_index=search_line)
      tmp_unit = int(unit_search.search(new_input[tmp_line_num]).groups()[0])
      if unit == tmp_unit:
        start_unit = tmp_line_num
        break
      else:
        search_line = tmp_line_num + 1
    end_unit = findLineNumWithComments(new_input,'boundary',start_index=start_unit)


    # Find where the array is described
    array_search = re.compile(r'array\s+(\d+)')
    for line_num in range(start_unit, end_unit):
      tmp_line_num = findLineNumWithComments(new_input,'array',start_index=line_num)
      possible_array = int(array_search.search(new_input[tmp_line_num]).groups()[0])
      if array_num == possible_array:
        array_line = tmp_line_num
        break
#    print new_input[array_line]

    # Read the array information
    array_reader = re.compile(r'array([a-zA-Z0-9.\-+ ]+)place')
    tmp_string = array_reader.search(new_input[array_line]).groups()[0]
    tmp_list = string2list(tmp_string)
    # The bounding surface for the array is the one that is not negative
    for i in range(1, len(tmp_list)):
      if tmp_list[i].find('-') == -1:
        array_surf = int(tmp_list[i])
#    print 'array surf is ', array_surf
    
    # Find the dimensions of the array surface being used
    x_plus = unitGeom[unit][array_surf]['dimension']['x+']
    x_minus = unitGeom[unit][array_surf]['dimension']['x-']
    y_plus = unitGeom[unit][array_surf]['dimension']['y+']
    y_minus = unitGeom[unit][array_surf]['dimension']['y-']
    surf_x_length = abs(x_plus - x_minus)
    surf_y_length = abs(y_plus - y_minus)

    # See if the array surface size is the same as the sum of the length of the units filling it
    if surf_x_length == array_size_x and surf_y_length == array_size_y:
      print 'Array', array_num, 'seems OK. Continuing...'
      pass
    else:
      print 'Array', array_num, ': The surface used to define the array is larger than the sum of the length of the units filling it.'
      print 'This will cause issues in KENO/MCDancoff.'
      print 'Attempting to fix the problem'
      x_diff = surf_x_length - array_size_x
      y_diff = surf_y_length - array_size_y
      if array_size_x == array_size_y:
        new_x_plus = x_plus - x_diff/2.0
        new_x_minus = x_minus + x_diff/2.0
        new_y_plus = y_plus - y_diff/2.0
        new_y_minus = y_minus + y_diff/2.0
      else:
        new_x_plus = x_plus - x_diff
        new_x_minus = x_minus
        new_y_plus = y_plus
        new_y_minus = y_minus + y_diff

      """ Start making the new surface for the array to be filled into """

      # Pick a new surface # that is not already in use
      tmp_list = unitGeom[unit].keys()
      new_surf_num = 999
      for num in range(999,0,-1):
        if new_surf_num in tmp_list:
          new_surf_num = new_surf_num - 1
        else:
          break

      # Make the new surface by copying the old one and editing it's values
      shape = unitGeom[unit][array_surf]['shape']
      array_surf_line = findLineNumWithComments(new_input, shape + ' ' + str(array_surf), start_index=start_unit)
      new_surf_list = string2list(new_input[array_surf_line])
#      print new_input[array_surf_line]
      new_surf_list[1] = str(new_surf_num)
      new_surf_list[2] = str(new_x_plus)
      new_surf_list[3] = str(new_x_minus)
      new_surf_list[4] = str(new_y_plus)
      new_surf_list[5] = str(new_y_minus)
      new_surf_definition = ' '.join(new_surf_list)
#      print new_surf_definition

      # Change the array definition to use the new surface
      new_array_list = string2list(new_input[array_line])
      # The bounding surface for the array is the one that is not negative
      for i in range(2, len(new_array_list)):
        if new_array_list[i].find('-') == -1:
          new_array_list[i] = str(new_surf_num)
          break
      new_array_definition = ' '.join(new_array_list)
#      print new_array_definition
      
      # Write the new surface definition to the input
      new_input.insert(array_surf_line, new_surf_definition + '\n')
      new_input.insert(array_surf_line, "'The new surface is defined below \n")

      # Write the new array definition to the input
      # Check if the array definition line number changed first
      if array_line > array_surf_line:
        array_line = array_line + 2
      new_input[array_line] = "'Old: " + new_input[array_line]
      new_input.insert(array_line, new_array_definition + '\n')
      new_input.insert(array_line, "'The new array is defined below \n")

      """ Now need to change the media that describes the original 
          surface number to also exclude the new surface number """
      # Find where the array is described, then append '-' + new_surf_num
      array_search = re.compile(r'array\s+(\d+)')
      for line_num in range(start_unit, end_unit):
        tmp_line_num = findLineNumWithComments(new_input,'media',start_index=tmp_line_num)
        tmp_list = string2list(new_input[tmp_line_num])
        if str(array_surf) in tmp_list[3:]:
          media_line = tmp_line_num
          tmp_list.append(' ' + '-' + str(new_surf_num))
          new_media_line = ' '.join(tmp_list)
          break
        else:
          tmp_line_num = tmp_line_num + 1

      new_input[media_line] = "'Old: " + new_input[media_line] + '\n'
      new_input.insert(media_line, new_media_line + '\n')
      new_input.insert(media_line, "'The new media is defined below \n")
  return new_input
