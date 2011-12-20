import sys
import re
from stringSearch import findLineNum, findLineNumWithComments, string2list

if __name__ == '__main__':
  pass

def editAboveCompositionBlock(new_input):

  print 'Running editAboveCompositionBlock'

  read_comp = findLineNumWithComments(new_input,'read comp')
  
  for line_num in range(read_comp):
    new_input[line_num] = "'/" + new_input[line_num]

  new_input.insert(0, "'batch_args \-m \n")
  new_input.insert(0, 'ce_v7_endf \n')
  new_input.insert(0, 'KENO input converted from NEWT \n')
  new_input.insert(0, '=csas6 parm=check \n')

  return new_input
