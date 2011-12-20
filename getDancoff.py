#!/usr/bin/python -tt

import sys
import glob
import re

def getDancoff(filename,skipped_lat_loc):    # filename contains multiple dancoff files

  """ IMPORTANT: NEWT and KENO read arrays in opposite order!!!
    For Example:
    For a 7 by 7 array, position 1,1,1 in NEWT is the top left corner of the lattice (first number you give it),
     however in KENO position 1,1,1 is the bottom right corner of the lattice (the last number you give it, 49th number in this case)
    """

  print 'Running getDancoff'

  file_list = glob.glob(filename)  # Expands * to find all dancoff files


  # this will read last numbers at the end of the filename ie blah.danc000010 will return 10
  read_lattice_loc = re.compile(r'danc[0]{2,}([0-9]{1,3})')   # looks for 'danc' then two to infinite zeros before finding one to three digits that may be nonzero

  dancoffByLoc = {}
  for each in file_list:         # loop which opens each dancoff file
    # Read the filename to determine the lattice location
    keno_lattice_loc = int(read_lattice_loc.search(each).groups()[0])
    newt_lattice_loc = len(file_list) + len(skipped_lat_loc) - 1 - keno_lattice_loc
    # These next 6 lines account for lattice_loc numbers that are skipped in the mcdanoff input because they have no fuel
    if len(skipped_lat_loc) > 0:
      num_skipped = 0
      for skipped_loc in skipped_lat_loc:
        if keno_lattice_loc >= skipped_loc:
          num_skipped = num_skipped + 1
      keno_lattice_loc = keno_lattice_loc + num_skipped
      newt_lattice_loc = newt_lattice_loc - num_skipped

    f = open(each, 'rU')
    lines = f.read().split('\n')    # Read all lines
    numL = len(lines)           # Count number of lines
    w = lines[0].split()
    if w[0] == 'Unit' and w[3] == 'global':
      loc_dict = {'x':float(w[5]),'y':float(w[7]),'z':float(w[9])}
      unit = int(w[1])
    elif w[0] == 'Unit' and w[3] != 'global':
        # need an example of this
      print "'global' not found in 1st line at 4th position"
    else:
      print "Keyword 'Unit' not found on 1st line at 1st position"

# now read dancoff factors and nuclide ID's from lines 3 to numL
    dan_dict = {}
    for i in range(2,numL-1):
      w = lines[i].split()
      dan_dict[int(w[1])] = w[2]
#  print 'dan_dict'
#  print dan_dict
    dancoffByLoc[newt_lattice_loc] ={'unit':unit,'location':loc_dict,'dancoffs':dan_dict}
  f.close()
  return dancoffByLoc

if __name__ == '__main__':
  print sys.argv[1:]
  print getDancoff(sys.argv[1:])
