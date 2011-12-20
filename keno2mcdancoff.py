import sys
import os
import re
from stringSearch import findLineNum, findLineNumWithComments
import subprocess
#from SPyT.Utilities.utils import *  # Used to get scale directory path

def keno2mcdancoff(data,filename):
  print 'Entering keno2mcdancoff'

  # Passed in all the accumulated data from the newt2keno routine
  new_input = data[0]
  compDataByMixtureID = data[1]
  mixAssignmentsGivenParentMix = data[2]
  parentMixGivenAssignedMix = data[3]
  unitGeom = data[4]
  unitsWithFuel = data[5]
  arrayData = data[6]
  fuelMixtures = data[7]

  # delete all lines below 'end bounds' and above 'end_data'
  end_bounds = findLineNumWithComments(new_input,'end boun')
  end_data = findLineNumWithComments(new_input,'end data',start_index=end_bounds)
  for i in range(end_bounds+1,end_data):
    new_input.remove(i)

  # Add the new block needed for MCDancoff  
  new_input.insert(end_bounds+1,'end start \n')
  new_input.insert(end_bounds+1,'read start \n')

  print arrayData[1].keys()
  print arrayData[1]['unitGivenLocation'].keys()
  print arrayData[1]['unitGivenLocation'][48]
  print unitsWithFuel
  print unitGeom[36].keys()
  print unitGeom[36][14].keys()
  print unitGeom[36][14]['shape']
  print unitGeom[36][14]['dimension']['x+']
  print unitGeom[36][13].keys()
  print unitGeom[36][13]['shape']

  # Go through each array, check if fuel is present
  counter = 0   # Used to keep track of which lattice elements don't have fuel
  skipped_lat_loc = [] # Used to keep track of which lattice elements don't have fuel
  for array_num in arrayData.keys():
    if arrayData[array_num]['fuel_present'] == 'yes':
      nux = arrayData[array_num]['nux']
      nuy = arrayData[array_num]['nuy']
      # Go through each unit inside the array, from last (bottom right) to first (top left)
      for newt_loc in range(len(arrayData[array_num]['unitGivenLocation'].keys())-1 , -1, -1):
        keno_loc = len(arrayData[array_num]['unitGivenLocation'].keys()) - 1 - newt_loc
        unit = arrayData[array_num]['unitGivenLocation'][newt_loc]
        if unit not in unitsWithFuel:
          new_input.insert(end_bounds+2,"'This unit has no fuel \n")
          skipped_lat_loc.append(counter)
#          skipped_lat_loc.append(loc)
# Change here, added this counter + 1 at 4:47 PM 12/19/11
          counter += 1
          continue
### Note this part will only work for square lattices currently
        else:
          counter = counter + 1
          # Determine x,y coordinates in array
          num = float(keno_loc+1)/nux
          diff = num - int((keno_loc+1)/nux)
          if diff == 0:
            y = int(num)
            x = nux
          else:
            y = int(num) + 1
            x = int(round(nux*diff))
          # Determine the outermost region containing fuel in the unit
          max_size = 0.0
          for surface in unitGeom[unit].keys():
            if surface == 'boundaryRegion': continue
            else:
              # Check if the region has fuel in it
              if unitGeom[unit][surface]['mixtureID'] not in fuelMixtures:
                continue
              else:
                if unitGeom[unit][surface]['shape'] == 'cylinder':
                  size = unitGeom[unit][surface]['radius']
                elif unitGeom[unit][surface]['shape'] == 'cuboid':
                  size = unitGeom[unit][surface]['dimension']['x+']
                else: print 'SHAPE THAT IS NOT SUPPORTED IN keno2mcdancoff with unit = ', unit, ' surface = ', surface
                # Check size
                if size > max_size:
                  max_size = size
                  region = unitGeom[unit][surface]['mediaOrder']
#        print region
        new_input.insert(end_bounds+2,'dancoff  array '+ str(array_num) + ' ' + str(x) + ' ' + str(y) + \
                    ' 1 ' + ' unit ' + str(unit) + ' region ' + str(region) + '\n')
      """ Reverse the order of the MCDancoff Start Data. This will account for the difference between NEWT and KENO array
        definitions when the Dancoff output files are read. Also, change the skipped_lat_loc list. """
      # Locate lines that have start data in them
#      read_start = findLineNumWithComments(new_input,'read start')
#      end_start = findLineNumWithComments(new_input,'end start')
#      tmp_list = new_input[read_start+1:end_start]
#      tmp_list.reverse()
#      new_input[read_start+1:end_start] = tmp_list
#
#      size = nux*nuy
#      print skipped_lat_loc
#      for num in range(len(skipped_lat_loc)):
#        skipped_lat_loc[num] = size - skipped_lat_loc[num]
#      print skipped_lat_loc


  # Change the sequence to mcdancoff and the library to xn01
  csas_line = findLineNumWithComments(new_input,'=csas')
  new_input.insert(csas_line, '=mcdancoff \n')
  del(new_input[csas_line + 1])

  library_line = findLineNumWithComments(new_input,'ce_v')
  new_input.insert(library_line, 'xn01 \n')
  del(new_input[library_line + 1])

# Write the mcdancoff input file
  new_filename = filename + '.mcdan.inp'
  g = open(new_filename, 'w')
  for line in new_input:
    g.write(line)
  g.close()

#  run_it(new_filename)

  return skipped_lat_loc









def run_it(new_filename):
  

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
  proc1 = subprocess.Popen(args)
  proc1.wait()




  
  
  
