#!/usr/bin/python -tt

import sys
import re
from depletionParser import parseDepletionBlock  # functions
from stringSearch import findLineNum
from getFuelMixtures import getFuelMixtures

if __name__ == '__main__':
#  print sys.argv[1:]
  print getUnitGeom(sys.argv[1])


def getUnitGeom(filename):

  latticeInfo = {}   # This is the dictionary which will contain Geometry and Mixture info for the lattice

# 1) should be able to read from an object, which units are in the array???
# if so then next is:

# 2) Know which mixtures numbers are fuels, get from some object
# 3) Read Media to determine what the geometry is, and which is outermost fuel


# if dealing with a legacy input which must be parsed, try this

# Delete comments
  f = open(filename, 'r')  
  lines = f.read().split('\n')    # Read all lines
  for line_num in range(len(lines)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if lines[line_num][0] == "'":
      del lines[line_num]         # delete the comments

# Find where the array block starts and ends
  start_array = findLineNum(lines,'read arr')
  end_array = findLineNum(lines,'end arr')
  print start_array
  print end_array

# Find nux and nuy to determine size of lattice
# There may be arrays for control blades, etc so loop
# through until nux = nuy (square array)
  read_nux = re.compile(r'^nux\D*(\d*)\b')
  read_nuy = re.compile(r'^nuy\D*(\d*)\b')
  nux = 0     # Initializing nux and nuy s.t. nux != nuy
  nuy = 1
  while nux != nuy:
    for line_num in range(start_array,end_array):
      loc = lines[line_num].find('nux')
      if loc != -1:
        nux = read_nux.search(lines[line_num][loc:]).groups()
        new_start = line_num        # will start searching for nuy here
        loc = -1
        break
#    print nux
    for line_num in range(start_array,end_array):
      loc = lines[line_num].find('nuy')
      if loc != -1:
        nuy = read_nuy.search(lines[new_start][loc:]).groups()
        new_start = line_num        # will start searching here next loop
        break

# Now the size of the lattice is known
# Read the units in. They are between keywords 'fill' and 'end'
  nux = int(nux[0])
  nuy = int(nuy[0])
  size = nux*nuy
  loc = -1
  unitByLocation = {}
  locationsByUnit = {}
  for line_num in range(new_start,end_array):
    loc = lines[line_num].find('fill')
    if loc != -1:
      new_start = line_num    # Will start looking at this line
      start_loc = loc + 4     # Will start looking after 'fill'
      loc = -1
      break
  for line_num in range(new_start,end_array):
    loc = lines[line_num].find('end')
    if loc != -1:
      new_end = line_num      # Will stop looking at this line
      end_loc = loc - 1       # Will stop looking before 'end'
      break
  all_lines = ' '
  for line_num in range(new_start,new_end + 1):
    if line_num == new_start:
      all_lines = lines[line_num][start_loc:]
    elif line_num == new_end + 1:
      all_lines = all_lines + ' ' + lines[line_num][:end_loc]
    else:
      all_lines = all_lines + ' ' + lines[line_num]
# Whole array is now one string. Parse for the unit numbers now. 
  read_units = re.compile(r'\d+')
  units_list = read_units.findall(all_lines)
  for pos in range(size):
    units_list[pos] = int(units_list[pos])
    unitByLocation[pos] = units_list[pos]
#!!  print units_list
#!!  print unitByLocation
# Make a dictionary that lists all locations where a given unit is located
  tmp_list = []
#  print 'len of units_list is ', len(units_list)
  for pos in range(size):
    tmp_list = []
    if units_list[pos] in locationsByUnit:
      continue
    else:
      tmp_list.append(pos)
      for num in range(pos + 1,size):
        if units_list[pos] == units_list[num]:
          tmp_list.append(num)
      locationsByUnit[units_list[pos]] = tmp_list
#!!  print locationsByUnit
  
#############################
# Maybe make a new file now #
#############################

# Find where the geometry block starts and ends
  start_geom = findLineNum(lines,'read g')
  end_geom = findLineNum(lines,'end g')

# Start interrogating each unit that is part of the lattice (in units_list)
  read_geom_unit = re.compile(r'(\d+)')
  for line_num in range(start_geom + 1, end_geom):
    if 'unit' not in lines[line_num]:
      continue
    else:
      unit = read_geom_unit.search(lines[line_num]).groups()
      unit = int(unit[0])
      if unit not in units_list:
        continue
      else:
#        print unit
        for new_line in range(line_num + 1, end_geom):
          j = -1
          j = lines[new_line].find('bound')
          if j != -1:
            end_of_unit = new_line
#            print end_of_unit
            break
# Now a unit which is in the lattice has been found and the lines describing the unit are known
# This section reads keywords(ie. cylinder, media) and makes a dictionary regionDict that
# Stores info for each region.
# When all data for all regions is assembled, regionDict is added to dictionary unitGeom
# for the appropriate unit
        regionDict = {}
        read_shorthand = re.compile(r'^(\d+)([sp])([a-zA-Z0-9.\-+]*)')   # ie for 4p5.43e-5 the returned list will contain ['4', 'p', '5.43e-5']
        media_counter = 1        # Initialize to 1 each time a new unit is parsed
        for new_line in range (line_num + 1, end_of_unit+1):
          geomData_tuple = re.split(',\s*|\s*', lines[new_line])
          geomData = list(geomData_tuple)          # convert the tuple into a list
          for i in range(len(geomData)-1, -1, -1):        # This loop removes any empty strings from geomData
            if geomData[i] == '':
              del geomData[i]
# Check for shorthand notation, if no shorthand is used then none will be returned.
# Need an exception for the error this will cause. If shorthand found, expand it.
          for i in range(len(geomData)-1, -1, -1):
            try:
              short = read_shorthand.search(geomData[i]).groups()
            except AttributeError:          # No shorthand, read it into dictionary
              continue
            else:
              num_r_or_p = int(short[0])
              geomData[i] = short[2]
              x = 0
              for z in range(i+1,i+num_r_or_p):
                if short[1] == 'p' and x%2 == 0:
                  geomData.insert(z,'-' + short[2])
                  x = x + 1
                else:
                  geomData.insert(z,short[2])
                  x = x + 1
# Now that the geometry data has been parsed and shorthand has been expanded, read the values in a dictionary
          if geomData[0] == 'cylinder':
            regionDict[int(geomData[1])] = {'shape':geomData[0], 'radius':float(geomData[2])}
          elif geomData[0] =='cuboid':
            regionDict[int(geomData[1])] = {'shape':geomData[0],'dimension':{'x+':float(geomData[2]),'x-':float(geomData[3]),'y+':float(geomData[4]),'y-':float(geomData[5])}}
# For 'media', we want to assign a mixtureID to a regionID. Select the regionID by whichever one is not negative.
          elif geomData[0] == 'media':
            for z in range(3,len(geomData)):
              j = geomData[z].find('-')
              if j == -1:  
                regionID = geomData[z]
                break
            regionDict[int(regionID)]['mixtureID'] = int(geomData[1])
            regionDict[int(regionID)]['mediaOrder'] = media_counter     # This is needed for MCDancoff Inputs
            media_counter += 1
            if float(geomData[2]) != 1.0:
              print 'Non-unity Density Multiplier in Unit ', unit, 'in region ', regionID
              print 'Value given is ', geomData[2]
              print 'WARNING - This is not accounted for yet when creating in Centrm Inputs '
          elif geomData[0] == 'boundary':
            latticeInfo[unit] = regionDict
#            print unitGeom
          else:
            continue
            print 'WARNING - Presently Unsupported Keyword In Unit ', unit
#        print regionDict
  print latticeInfo[11]

  fuelMixtures = getFuelMixtures(lines)
  print fuelMixtures
  mixtureAssignments = parseDepletionBlock(lines)


