import sys
import re
from stringSearch import findLineNum, findLineNumWithComments, string2list
from getCompositionData import getCompDataByMixtureID
from getDepletionData import getMixtureAssignments

def addAssignments2CompBlock(lines,compDataByMixtureID=0, mixAssignmentsGivenParentMix=0):

########################################################################
# Append the commented input in the composition block with mixture ID's 
# that are assigned in triton, and thus not in the composition block
########################################################################

  print 'Running addAssignments2CompBlock'

  if compDataByMixtureID == 0:
    compDataByMixtureID = getCompDataByMixtureID(lines)
  if mixAssignmentsGivenParentMix == 0:
    tmp_list = getMixtureAssignments(lines)
    mixAssignmentsGivenParentMix = tmp_list[1]

  start_comp = findLineNumWithComments(lines,'read comp')
  end_comp = findLineNumWithComments(lines,'end comp',start_index=start_comp)

  new_lines = []  # These are what will be appended to the composition block
  new_lines.append("'")
  new_lines.append("'" + 'Begin Making Compositions for Assigned Mixtures from the Triton Depletion Block')
  for parentMix in mixAssignmentsGivenParentMix.keys():
    assignedMixList = mixAssignmentsGivenParentMix[parentMix]
    new_lines.append("'"+'These Compositions are Assignments for Mixture ' + str(parentMix) + ' in Triton')
    for assignedMix in assignedMixList:
      for materialIndex in compDataByMixtureID[parentMix].keys():
        tmp_list = compDataByMixtureID[parentMix][materialIndex][:]  # The [:] is there to make a new copy of the list, not just a new variable that points at the same data
        tmp_list[1] = str(assignedMix)    # Replacing the parentMix with the assignedMix
        new_lines.append(' '.join(tmp_list))   # The list of strings is joined into one string (separated by ' ') and appended to new_lines
  
# Insert the new composition lines into the input
  new_input = lines[:]
  for line_num in range(len(new_lines)-1,-1,-1):
    new_input.insert(end_comp, new_lines[line_num] + '\n')
  return new_input
  



if __name__ == '__main__':
  f = open(sys.argv[1], 'r')  
  lines = f.read().split('\n')    # Read all lines
  addAssignments2CompBlock(lines)


