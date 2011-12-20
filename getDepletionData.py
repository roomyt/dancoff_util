import sys
import re
from stringSearch import findLineNum, string2list

def getMixtureAssignments(lines):
############################################################################
# If the 'assign' keyword is used in the Depletion Block, this routine
# determines which mixture ID's are assigned so that they can be added
# to the composition block for the MCDancoff Input.

# If no assignments are present, set mixAssignmentsGivenParentMix = -1

  print 'Running getMixtureAssignments in getDepletionData'

#  mixAssignmentsGivenParentMix = {}   # This is the dictionary which will hold {mixtureID : [Assigned MixtureIDs]}
#  parentMixGivenAssignedMix = {}  # This dictionary holds {Assigned mixture ID : Parent mixture ID}

  mixAssignmentsGivenParentMix = -1
  parentMixGivenAssignedMix = -1

# Make sure comments are removed
  for line_num in range(len(lines)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if lines[line_num][0] == "'":
      del lines[line_num]         # delete the comments

# Check if depletion block exists
  start_depl = findLineNum(lines,'read dep')
  if start_depl == -1:
    print 'No Depletion Block Found: There are no mixtureID assignments'
  else:

    end_depl = findLineNum(lines,'end dep', start_index=start_depl)

  # Make into one long string
    all_lines = ' '
    for line_num in range(start_depl,end_depl+1):
      all_lines = all_lines + lines[line_num] + ' '

  # If assignments are present in the depletion block, then fill the dictionaries
    if 'assign' in all_lines:
      mixAssignmentsGivenParentMix = {}
      parentMixGivenAssignedMix = {}
    # Separate each word/number into a list
      depl_block = string2list(all_lines)
    # Now look for the keyword 'assign' to determine which mixtures aren't in the composition block
      for i in range(len(depl_block)):
        if depl_block[i] == 'assign':
          tmp_list = []
          for j in range(i+2, len(depl_block)):
            if depl_block[j] == 'end':
              mixAssignmentsGivenParentMix[int(depl_block[i+1])] = tmp_list
              for assignedMix in tmp_list:
                parentMixGivenAssignedMix[assignedMix] = int(depl_block[i+1])
              break
            else:
              tmp_list.append(int(depl_block[j]))
# Return the dictionaries
  data = [parentMixGivenAssignedMix, mixAssignmentsGivenParentMix]
  return data
  


if __name__ == '__main__':
  f = open(sys.argv[1], 'r')  
  lines = f.read().split('\n')    # Read all lines
  for line_num in range(len(lines)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if lines[line_num][0] == "'":
      del lines[line_num]         # delete the comments
  getMixtureAssignments(lines)


