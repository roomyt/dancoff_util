#!/usr/bin/python -tt

import sys
import re
from stringSearch import findLineNum, findLineNumWithComments
from getCompositionData import getCompDataByMixtureID
from editAboveCompositionBlock import editAboveCompositionBlock
from editGeomBlock import editGeomBlock
from editArrayBlock import editArrayBlock
from editBoundsBlock import editBoundsBlock
from editBottomOfNewtInput import editBottomOfNewtInput
from fixUnitsWithArrays import fixUnitsWithArrays
from getUnitGeom import getUnitGeom
from getArrayData import getArrayData
from getFuelMixtures import getFuelMixtures
from addAssignments2CompBlock import addAssignments2CompBlock
from getUnitsWithFuel import getUnitsWithFuel
from getDepletionData import getMixtureAssignments
from subprocess import Popen
#from SPyT.Utilities.utils import *  # Used to get scale directory path

def newt2keno(filename):

  """ This module converts a newt input into a keno input. Two main steps are taken:
      I.) Parse the input for information about the problem
         A) Read geometry and media information for each unit
         B) Read array definition data
         C) Determine which units have fuel in them
            1) Determine which mixture ID's have fuel in them
               i) Read composition data
               ii) Read assignments from the depletion block
      II.) Edit the input to convert from Newt to KENO style input """

# Read the input
  f = open(filename, 'r')  
  lines = f.read().split('\n')    # Read all lines
  f.close()

# Read Composition Data
  compDataByMixtureID = getCompDataByMixtureID(lines)

# Find mixture assignments if present
  mixData = getMixtureAssignments(lines)
  parentMixGivenAssignedMix = mixData[0]
  mixAssignmentsGivenParentMix = mixData[1]

# Determine which mixture ID's have fuel in them
  fuelMixtures = getFuelMixtures(lines,compDataByMixtureID,mixAssignmentsGivenParentMix)

# Read geometry and media information for each unit
  unitGeom = getUnitGeom(lines)

# Determine which units have fuel
  unitsWithFuel = getUnitsWithFuel(lines,fuelMixtures)

# Read array data
  arrayData = getArrayData(lines,unitsWithFuel)

  """ Start Making a New Input File """
# If Assigned Mixtures are Used, Add them to the Composition Block
  if mixAssignmentsGivenParentMix != -1:
    new_input = addAssignments2CompBlock(lines,compDataByMixtureID,mixAssignmentsGivenParentMix)

# Edit the computational sequence, title, and cross-section library
  new_input = editAboveCompositionBlock(new_input)

# Remove all input between the composition block and the geometry block
  end_comp = findLineNumWithComments(new_input, 'end comp')
  read_geom = findLineNumWithComments(new_input, 'read geom')
  for count in range(read_geom - end_comp - 1):
    del(new_input[end_comp+1])

# Add a parameter block after the composition block
  new_input.insert(end_comp+1,'end parm \n')
  new_input.insert(end_comp+1,'     nsk=0 \n')
  new_input.insert(end_comp+1,'     npg=500 \n')  #500 is probably too much
  new_input.insert(end_comp+1,'     gen=100 \n')  #100 probably good
  new_input.insert(end_comp+1,'     htm=no \n')
  new_input.insert(end_comp+1,'read parm \n')

# Make adjustments to Geometry Block 
  new_input = editGeomBlock(new_input)

# Make adjustments to Array Block
  new_input = editArrayBlock(new_input)

# Make sure bounds are correct
  new_input = editBoundsBlock(new_input)

# Remove "end model" and add "end data". 
# Also delete anything between "end bounds" and "end data" except for a plot block
  new_input = editBottomOfNewtInput(new_input)

# Attempt to fix how arrays are placed in the newt model geometry
  new_input = fixUnitsWithArrays(new_input,unitGeom,arrayData)

# Have to add back \n to lines that don't have them
  for line_num in range(len(new_input)):
    if '\n' not in new_input[line_num]:
      new_input[line_num] = new_input[line_num] + '\n'

# Write the keno input file
  new_filename = filename + '.keno.inp'
  g = open(new_filename, 'w')
  for line in new_input:
    g.write(line)
    
  g.close()

#  run_it(new_input,new_filename)

  print arrayData[1].keys()
  print arrayData[1]['unitGivenLocation'].keys()
# Return Information
  data = [new_input,compDataByMixtureID,mixAssignmentsGivenParentMix,
          parentMixGivenAssignedMix,unitGeom,unitsWithFuel,arrayData,fuelMixtures]
  return data





def run_it(new_input,new_filename):

  # Find the scale_path and version
  scale_path = get_scale_root()
  find_version = re.compile(r'scale(\d+.\d+)')
  version = find_version.search(scale_path).groups()[0]

# Setup the arguments needed to run Scale
  args = []
  if '/' in scale_path:
    machine = 'posix'
    args.append(scale_path + '/cmds/batch' + version)
  else:
    machine = 'windows'
    args.append(scale_path + '\cmds\batch' + version + '.bat')
  args.append(' -m ')
  args.append(new_filename)

# Run Scale
  proc1 = Popen(args)
  proc1.wait()







if __name__ == '__main__':
# Read file, keeping the comments
#  f = open(sys.argv[1], 'r')  
#  lines = f.read().split('\n')    # Read all lines
#  f.close()
#  newt2keno(lines)
  newt2keno(sys.argv[1])

