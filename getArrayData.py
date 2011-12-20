import sys
import re
from stringSearch import findLineNum
from getUnitsWithFuel import getUnitsWithFuel


def getArrayData(lines,unitsWithFuel=0):

  print 'Running getArrayData'

  for line_num in range(len(lines)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if lines[line_num][0] == "'":
      del lines[line_num]         # delete the comments

  if unitsWithFuel == 0:
    unitsWithFuel = getUnitsWithFuel(lines)

  arrayData = {}
  unitGivenLocation = {}
  locationsGivenUnit = {}

# Find where the array block starts and ends
  start_array = findLineNum(lines,'read arr')
  end_array = findLineNum(lines,'end arr',start_index=start_array)

# Merge the Array block into 1 line, remove excess spaces
  array_block = ' '.join(lines[start_array:end_array + 1])
  array_block = re.sub('\s+',' ', array_block)
 

# Expand any FIDO style input that may be present
# Need an exception for the error this will cause. If FIDO input found, expand it.
  read_fido = re.compile(r'((\d+)([rp])([a-zA-Z0-9.\-+]*))')   # ie for 4p5.43e-5 the returned list will contain ['4p5.43e-5', '4', 'p', '5.43e-5']
  for i in range(100):
    try:
      fido = read_fido.search(array_block).groups()
    except AttributeError:          # No FIDO found, exit loop
      break
    else:
      num_r_or_p = int(fido[1])
      tmp_list = array_block.split(fido[0])
      new_string = ''
      if fido[2] == 'r':
        for num in range(int(fido[1])):
          new_string = new_string + fido[3] + ' '
      array_block = tmp_list[0] + new_string + tmp_list[1]


  """ For each array, read the array #, nux, nuy, and type.
    Then from keywords 'fill' to 'end' read in the units for the array """
  read_ara = re.compile(r'ara\D+(\d+)\b')
  read_nux = re.compile(r'nux\D+(\d+)\b')
  read_nuy = re.compile(r'nuy\D+(\d+)\b')
  read_typ = re.compile(r'typ[ =]*(\w*)\b')
  read_fill = re.compile(r'fill\s+\d+')

  """ 1) Determine how many arrays there are.
      2) Use keyword 'ara' to navigate the array definitions.
         a) Split the array_block at 'ara' so that each array definition is isolated
         b) Read 'nux', 'nuy' and 'typ' into dictionary arrayData for each array
      3) Store the unit numbers that belong to each array in a dictionary
         a) Begin reading unit numbers after keyword 'fill'
         b) Dictionaries unitGivenLocation and locationsGivenUnit will be
            populated and then added to the dictionary arrayData. """
  array_numbers = []
  ara_indices = []
  fill_indices = []
  arrays = []
  for array in read_ara.finditer(array_block):
    array_numbers.append(int(array.groups()[0]))
# Split each array definition into a spearate string
  arrays = array_block.split('ara')
  del(arrays[0])
  
  for num in range(len(array_numbers)):
    ara = array_numbers[num]
    nux = int(read_nux.search(arrays[num]).groups()[0])
    nuy = int(read_nuy.search(arrays[num]).groups()[0])
    test4type = -1
    test4type = arrays[num].find('typ')
    if test4type != -1:
      typ = read_typ.search(arrays[num]).groups()[0]
    else:
      typ = 'cuboidal'  # This is the default in Scale
    arrayData[ara] = {'nux':nux, 'nuy':nuy, 'typ':typ}

  """ Now that the size and shape of each array is known, read in all the
      units for each array. These units will be stored in three different ways:
        1) In a list called unitsList
        2) In a dictionary called unitGivenLocation
        3) In a dictionary called locationsGivenUnit
      These three data structures will be convenient for other modules to rely on.
      Begin reading unit numbers after the fill_index for each array.
      The number of units will be nux*nuy """
  read_units = re.compile(r'(\d+)[ ,]*')
  for num in range(len(array_numbers)):
    units_list = []
    unitGivenLocation = {}
    locationsGivenUnit = {}
    fill_index = arrays[num].find('fill')
    units_list = read_units.findall(arrays[num][fill_index:])
    size = arrayData[array_numbers[num]]['nux']*arrayData[array_numbers[num]]['nuy']
    if size != len(units_list):
      print 'Error - nux*nuy is not equal to the number of units entered in array ', ara
      exit
    for position in range(size):
      units_list[position] = int(units_list[position])
      unitGivenLocation[position] = units_list[position]
    tmp_list = []
    for position in range(size):
      tmp_list = []
      if units_list[position] in locationsGivenUnit:
        continue
      else:
        tmp_list.append(position)
        for num2 in range(position + 1,size):
          if units_list[position] == units_list[num2]:
            tmp_list.append(num2)
        locationsGivenUnit[units_list[position]] = tmp_list
    arrayData[array_numbers[num]]['units_list'] = units_list
    arrayData[array_numbers[num]]['unitGivenLocation'] = unitGivenLocation
    arrayData[array_numbers[num]]['locationsGivenUnit'] = locationsGivenUnit

  """ Now use unitsWithFuel so that it can be determined if an array has fuel
      in it. Add {'fuel_present' : zzz} to each array in arrayData. zzz is 'yes' or 'no'. """
  for num in array_numbers:
    arrayData[num]['fuel_present'] = 'no'
    for unit in arrayData[num]['units_list']:
      if unit in unitsWithFuel:
        arrayData[num]['fuel_present'] = 'yes'
        break

  """ Now determine in what units the arrays are used in. Add this information
      to the dictionary arrayData. """
  # Find where the array block starts and ends
  start_geom = findLineNum(lines,'read geom')
  end_geom = findLineNum(lines,'end geom',start_index=start_geom)

  array_search = re.compile(r'array\s+(\d+)')
  unit_search = re.compile(r'unit\s+(\d+)')
  for line in lines[start_geom : end_geom]:
    if line.find('unit') != -1:
      unit = int(unit_search.search(line).groups()[0])
    if line.find('array') != -1:
      array_num = int(array_search.search(line).groups()[0])
      arrayData[array_num]['locatedInUnit'] = unit


  print arrayData[200]['locatedInUnit']
  return arrayData
      


if __name__ == '__main__':
  f = open(sys.argv[1], 'r')  
  lines = f.read().split('\n')    # Read all lines
  for line_num in range(len(lines)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if lines[line_num][0] == "'":
      del lines[line_num]         # delete the comments
  getArrayData(lines)
