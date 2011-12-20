import sys
import re
from stringSearch import findLineNum, findLineNumWithComments, string2list

if __name__ == '__main__':
  pass

def editArrayBlock(new_input):

# This module addresses changes needed for the array block in order to convert
# from Newt to Keno. The adjusted input is then returned.
#
# Adds 'nuz=1' for any arrays and removes any pinpow statements if present


# NOTE: if many exceptions in the input begin breaking this code. It may be more
#    robust to read only the things wanted (nux=9, fill, end fill, etc) 
#    r'^nux\D*(\d*)\b'   for example to get nux, then insert nuz=1

  print 'Running editArrayBlock'
  
  read_array = findLineNumWithComments(new_input, 'read arra')
  end_array = findLineNumWithComments(new_input, 'end arra',start_index=read_array)

# This adds 'nuz=1' to any arrays
  for line_num in range(read_array + 1, end_array):
    if 'ara' in new_input[line_num]:
      for new_line in range(line_num, end_array):
        if 'nuy' in new_input[new_line] and 'nuz' not in new_input[new_line]:
          tmp_list = string2list(new_input[new_line])
          for index in range(len(tmp_list)):
            if 'nuy' in tmp_list[index]:
              tmp_list.insert(index,'nuz=1')
              new_input[new_line] = '  '.join(tmp_list) + '\n'
              break



# This removes a pinpow statement if present
  for line_num in range(read_array + 1, end_array):
    if 'ara' in new_input[line_num]:
      for new_line in range(line_num, end_array):
        if 'pinpow' in new_input[new_line]:
          tmp_list = string2list(new_input[new_line])
          for index in range(len(tmp_list)):
            if 'pinpow' in tmp_list[index]:
              del(tmp_list[index])
              if '=' in tmp_list[index] or 'yes' in tmp_list[index] or 'no' in tmp_list[index]:
                del(tmp_list[index])
                if 'yes' in tmp_list[index] or 'no' in tmp_list[index]:
                  del(tmp_list[index])
                  new_input[new_line] = ' '.join(tmp_list[:]) + '\n'
                  break
                else:
                  new_input[new_line] = ' '.join(tmp_list[:]) + '\n'
                  break

                  
  return new_input

