import sys
import re
from stringSearch import findLineNum, string2list
from expandFIDO import expandFIDO

def parseGeometryKeywords(list_of_strings, unit):
  """ Given (1) a list of strings that define the geometry of a unit and (2) the
      unit number, this module will create a dictionary 'regionDict' that
      summarizes the unit geometry.
      This regionDict is then returned. """

#  print 'Running parseGeometryKeywords'

  regionDict = {}  # Temporary dictionary for holding data to be added to unitGeom

  media_counter = 1        # Initialize to 1 each time a new unit is parsed
  for new_line in range(len(list_of_strings)):
# Split the string new_line into a list of words/numbers called geomData
    geomData = string2list(list_of_strings[new_line])
    """ Check for shorthand notation, if no shorthand is used then none will be returned.
        Need an exception for the error this will cause. If shorthand found, expand it. """
    geomData = expandFIDO(geomData)
# Now that the geometry data has been parsed and shorthand has been expanded, read the values in a dictionary
    if not geomData: # skip if there is a blank line
      continue   
    elif geomData[0] == 'cylinder':
      regionDict[int(geomData[1])] = {'shape':geomData[0], 'radius':float(geomData[2])}
    elif geomData[0] =='cuboid':
      regionDict[int(geomData[1])] = {'shape':geomData[0],'dimension':{'x+':float(geomData[2]),'x-':float(geomData[3]),'y+':float(geomData[4]),'y-':float(geomData[5])}}
# For 'media', we want to assign a mixtureID to a regionID. Select the regionID by whichever one is not negative.
# Search among geomData[3:] since this is where composition numbers start
    elif geomData[0] == 'media':
      for z in range(3,len(geomData)):
        j = geomData[z].find('-')
        if j == -1:  
          regionID = geomData[z]
          break
      regionDict[int(regionID)]['mixtureID'] = int(geomData[1])
      regionDict[int(regionID)]['mediaOrder'] = media_counter     # This is needed for MCDancoff Inputs
      regionDict[int(regionID)]['densityMultiplier'] = float(geomData[2])
      media_counter += 1
      if float(geomData[2]) != 1.0:
        print 'Non-unity Density Multiplier in Unit ', unit, 'in region ', regionID
        print 'Value given is ', geomData[2]
        print 'WARNING - This is not accounted for yet when creating in Centrm Inputs '
    elif geomData[0] == 'hole':
      media_counter += 1
      print 'WARNING - Hole found in unit ', unit, '.  Nothing currently done with holes.'
    elif geomData[0] == 'boundary':
      regionDict['boundaryRegion'] = int(geomData[1])
#      unitGeom[unit] = regionDict
    elif geomData[0].find('com') != -1:
      continue  # This is just a comment
    else:
      continue
      print 'WARNING - Presently Unsupported Keyword In Unit ', unit
#      print regionDict
  return regionDict
