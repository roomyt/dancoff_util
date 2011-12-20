import sys
import re
from stringSearch import findLineNum, findLineNumWithComments, string2list

if __name__ == '__main__':
  pass

def editGeomBlock(new_input):
  """ This module addresses changes needed for the geometry block in order to convert
   from Newt to Keno. The adjusted input is then returned.

   This module adds a z-dimension to the shapes that are described
   It removes any grid information from the "boundary" statement
   It adds an index and a position for the z-dimension for arrays

   Shorthand notation is identified if present for cuboids

   Note that '  '.join(tmp_list[0:x]) joins together elements 0 to x-1, with '  ' in between each element
  """

  print 'Running editGeomBlock'

  read_geom = findLineNumWithComments(new_input, 'read geom')
  end_geom = findLineNumWithComments(new_input, 'end geom',start_index=read_geom)
# In case some shorthand notation is used
  read_shorthand = re.compile(r'^(\d+)([sp])([a-zA-Z0-9.\-+]*)')   # ie for 4p5.43e-5 the returned list will contain ['4', 'p', '5.43e-5']


  for line_num in range(read_geom + 1, end_geom):
########### Cylinder
    if 'cylinder' in new_input[line_num]:
      tmp_list = string2list(new_input[line_num])
      new_input[line_num] = '  '.join(tmp_list[0:3]) + '  20.0  -20.0  '+ '  '.join(tmp_list[3:]) + '\n'
########### Cuboid
    elif 'cuboid' in new_input[line_num]:
      tmp_list = string2list(new_input[line_num])
      try:
        short = read_shorthand.search(tmp_list[2]).groups()
      except AttributeError:   # No shorthand used
        new_input[line_num] = '  '.join(tmp_list[0:6]) + '  20.0  -20.0  '+ '  '.join(tmp_list[6:]) + '\n'
      else:                    # There was shorthand
        new_input[line_num] = '  '.join(tmp_list[0:3]) + '  20.0  -20.0  '+ '  '.join(tmp_list[3:]) + '\n'
############ Boundary
    elif 'boundary' in new_input[line_num]:
      tmp_list = string2list(new_input[line_num])
      new_input[line_num] = 'boundary  ' + tmp_list[1] + '\n'
############ Array
    elif 'array' in new_input[line_num]:
      tmp_list = string2list(new_input[line_num])
      new_input[line_num] = '  '.join(tmp_list[0:6]) + '  1  ' + '  '.join(tmp_list[6:8]) + '  0.0  ' + '  '.join(tmp_list[8:]) + '\n'

  return new_input

