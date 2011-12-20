import sys
import re

def expandFIDO(list_):
  """ Given a list of strings, this function will check each element for FIDO
      style input and expand it if found. """

  read_shorthand = re.compile(r'^(\d+)([rp])([a-zA-Z0-9.\-+]*)')
  # ie for 4p5.43e-5 the returned list will contain ['4', 'p', '5.43e-5']
  
  for i in range(len(list_)-1, -1, -1):
     try:
       short = read_shorthand.search(list_[i]).groups()
     except AttributeError:          # No shorthand, read it into dictionary
       continue
     else:
       num_r_or_p = int(short[0])
       list_[i] = short[2]
       x = 0
       for z in range(i+1,i+num_r_or_p):
         if short[1] == 'p' and x%2 == 0:
           list_.insert(z,'-' + short[2])
           x = x + 1
         else:
           list_.insert(z,short[2])
           x = x + 1
  return list_
