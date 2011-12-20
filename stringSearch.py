import sys
import re

if __name__ == '__main__':
  pass

def findLineNum(list_to_search,string_of_interest,start_index=0):
  line_of_interest = -1
  j = -1
  for line_num in range(start_index,len(list_to_search)-1):
    j = list_to_search[line_num].find(string_of_interest)
    if j != -1:
      line_of_interest = line_num
      break
# check if the string was found
  if line_of_interest != -1:
    return line_of_interest
  else:
    print 'WARNING'
    print 'The string ', string_of_interest, ' was not found'
    return line_of_interest

###################################################################################

def findLineNumWithComments(list_to_search,string_of_interest,start_index=0):
  line_of_interest = -1
  j = -1
  for line_num in range(start_index,len(list_to_search)-1):
    if list_to_search[line_num][0] == "'":
      continue
    else:
      j = list_to_search[line_num].find(string_of_interest)
      if j != -1:
        line_of_interest = line_num
        break
# check if the string was found
  if line_of_interest != -1:
    return line_of_interest
  else:
    print 'WARNING'
    print 'The string ', string_of_interest, ' was not found'
    return line_of_interest

#################################################################################
# Separate each word/number into a list

def string2list(the_string):
  the_tuple = re.split(',\s*|\s*', the_string)
  the_list = list(the_tuple)         # Convert the tuple into a list for easier manipulation
  for i in range(len(the_list)-1, -1, -1):        # This loop removes any empty strings from the_list
    if the_list[i] == '':
      del the_list[i]
#  print 'from string2list ',the_list
  return the_list

