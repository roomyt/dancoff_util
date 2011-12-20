#!/usr/bin/python -tt

import sys
import re
from stringSearch import findLineNum, findLineNumWithComments, string2list

def getCompDataByMixtureID(lines):
  compDataByMixtureID = {}
  """ dictionary compDataByMixtureID will contain 
  {mixID : {materialIndex : [list of strings for the composition data]}}
  where mixID and materialIndex are integers. An example is below:

  uo2 500 den=10.19 0.97 948.45 92235 2.93 92234 0.0261 92236 0.0135 92238 97.0304 end
  gd2o3 500 den=10.19 0.03 948.45 end

  This would be stored as follows:
  {500 :{0 :['uo2', '500', 'den=10.19', '0.97', ... , 'end']}, {1 :['gd2o3', '500', 'den=10.19', '0.03', '948.45', 'end']}}
  """

  print 'Running getCompDataByMixtureID in getCompositionData'

  linesNoComm = lines[:]
  for line_num in range(len(linesNoComm)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if linesNoComm[line_num][0] == "'":
      del linesNoComm[line_num]         # delete the comments

  start_compNoComm = findLineNum(linesNoComm,'read comp')
  end_compNoComm = findLineNum(linesNoComm,'end comp',start_index=start_compNoComm)

# Need to add materials to the composition block that were "assigned" in the depletion block of the Newt input

  compString = ''
  for line_num in range(start_compNoComm+1, end_compNoComm):
    if 'end' not in linesNoComm[line_num]:
      compString = compString + linesNoComm[line_num] + ' '
      continue
    else:
      compString = compString + linesNoComm[line_num]
      compData_list = string2list(compString)
      compString = ''
# A mixture ID may be made of several materials, account for that here
# If the mixture ID already exists then add a new material (index for materials counts up from 0)
      mixID = int(compData_list[1])
      if int(compData_list[1]) not in compDataByMixtureID.keys():
        compDataByMixtureID[mixID] = {0:compData_list}
      else:
        materialIndex = len(compDataByMixtureID[mixID].keys())  # If 0 is already taken, then len will return 1, which is used for the materialIndex
        compDataByMixtureID[mixID][materialIndex] = compData_list
  return compDataByMixtureID


if __name__ == '__main__':
  f = open(sys.argv[1], 'r')  
  lines = f.read().split('\n')    # Read all lines
  getCompDataByMixtureID(lines)
