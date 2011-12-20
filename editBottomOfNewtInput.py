import sys
import re
from stringSearch import findLineNum, findLineNumWithComments, string2list

if __name__ == '__main__':
  pass

def editBottomOfNewtInput(new_input):
  """ editBottomOfNewtInput(new_input):
   This module addresses changes needed below the bounds block in order to convert
   from Newt to Keno. The adjusted input is then returned.

   Remove "end model" and add "end data". 
   Also delete anything between "end bounds" and "end data" except for a plot block
  """

  print 'Running edit BottomOfNewtInput'

  end_bounds = findLineNumWithComments(new_input, 'end bounds')
  end_model = findLineNumWithComments(new_input, 'end mod',start_index=end_bounds)

# insert "end data" and delete "end model"
  new_input.insert(end_model+1,'end data\n')
  del(new_input[end_model:end_model+1])

# Delete everything BETWEEN "end bounds" and "end data"
  del(new_input[end_bounds+1:end_model])

  return new_input

