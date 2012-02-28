import sys
import re
from stringSearch import findLineNum
from getCompositionData import getCompDataByMixtureID
from getMixtureAssignments import getMixtureAssignments
#from SPyT.StdCompLib.StdCompLib import *

#def newOne(lines):

#  fuelMixtures = []        # List that will contain mixture ID's that have fuel
#  compDataByMixtureID = getCompDataByMixtureID(lines)
# This is a dictionary of form {mixID:{materialIndex:[list of strings that describe the composition]}}
# Further described in module getCompDataByMixtureID

#  for mixID in compDataByMixtureID.keys():
#    for materialIndex in range(len(compDataByMixtureID[mixID])):
      





def getFuelMixtures(lines,compDataByMixtureID=0,mixAssignmentsGivenParentMix=0):

  for line_num in range(len(lines)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if lines[line_num][0] == "'":
      del lines[line_num]         # delete the comments

  print 'Running getFuelMixtures'

# This determines which mixtures are fuels
# Find where the composition block starts and ends
  fuelMixtures = []        # List that will contain mixture ID's that have fuel

  fuelNames = ['uo2','92235','92238','92000','u-235','u-238','u-233','uranium','u','uc','un','u3o8','u(.27)metal']

  if compDataByMixtureID == 0:
    compDataByMixtureID = getCompDataByMixtureID(lines)
# This is a dictionary of form {mixID:{materialIndex:[list of strings that describe the composition]}}
# Further described in module getCompDataByMixtureID
  if mixAssignmentsGivenParentMix == 0:
    assignmentData = getMixtureAssignments(lines)
    mixAssignmentsGivenParentMix = assignmentData[1]


  for mixID in compDataByMixtureID.keys():
    for materialIndex in range(len(compDataByMixtureID[mixID])):
      for fuelName in fuelNames:
        if fuelName in compDataByMixtureID[mixID][materialIndex]:
          if mixID not in fuelMixtures:
            fuelMixtures.append(mixID)
            break

# Replace any mixtureIDs with their assignments if present.
# Work through fuelMixtures backwards.
  if mixAssignmentsGivenParentMix != -1:
    for index in range(len(fuelMixtures)-1,-1,-1):
      if fuelMixtures[index] in mixAssignmentsGivenParentMix.keys():
        assignedMixs = mixAssignmentsGivenParentMix[fuelMixtures[index]]
        del fuelMixtures[index]
        for assignedMix in assignedMixs:
          fuelMixtures.insert(index,assignedMix)

  return fuelMixtures 

if __name__ == '__main__':
  f = open(sys.argv[1], 'r')  
  lines = f.read().split('\n')    # Read all lines
  for line_num in range(len(lines)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if lines[line_num][0] == "'":
      del lines[line_num]         # delete the comments
  getFuelMixtures(lines)
