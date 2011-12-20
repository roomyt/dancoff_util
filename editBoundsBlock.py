import sys
import re
from stringSearch import findLineNum, findLineNumWithComments, string2list

if __name__ == '__main__':
  pass

def editBoundsBlock(new_input):

# This module checks to see if boundary conditions are set to all reflective.
# If they are not, then "all=refl" is inserted and a message is printed

  print 'Running editBoundsBlock'

  read_bounds = findLineNumWithComments(new_input, 'read bou')
  end_bounds = findLineNumWithComments(new_input, 'end bou')
  all_refl = 0
  for line_num in range(read_bounds + 1, end_bounds):
    if 'all' in new_input[line_num]:
      all_refl = 1
  if all_refl == 0:
    del(new_input[read_bounds + 1: end_bounds])
    new_input.insert(read_bounds+1, 'all=refl')
    print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    print 'BOUNDARIES SET TO ALL REFLECTIVE'
    print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

  return new_input

