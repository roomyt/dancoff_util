import sys
import re
from stringSearch import findLineNum


def getLatticeUnits(lines):

# Find where the array block starts and ends
  start_array = findLineNum(lines,'read arr')
  end_array = findLineNum(lines,'end arr',start_index=start_array)

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

  latticeList = [units_list,unitByLocation,locationsByUnit]
  return latticeList


if __name__ == '__main__':
  f = open(filename, 'r')  
  lines = f.read().split('\n')    # Read all lines
  for line_num in range(len(lines)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if lines[line_num][0] == "'":
      del lines[line_num]         # delete the comments
  getLatticeUnits(lines)
