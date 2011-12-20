import sys
import re
from newt2keno import newt2keno
from keno2mcdancoff import keno2mcdancoff
from getDancoff import getDancoff
from analyzeDancoffs import analyzeDancoffs
from makeDancoffMap import makeDancoffMap

def myProgram(filename,dan_tolerance=0.01):

  dan_tolerance = 0.01

  data = newt2keno(filename)
  new_input = data[0]
  compDataByMixtureID = data[1]
  mixAssignmentsGivenParentMix = data[2]
  parentMixGivenAssignedMix = data[3]
  unitGeom = data[4]
  unitsWithFuel = data[5]
  arrayData = data[6]
  fuelMixtures = data[7]

  skipped_lat_loc = keno2mcdancoff(data,filename)
  print filename + '.mcdan.danc*'
  dancoffByLoc = getDancoff(filename + '.mcdan.danc*',skipped_lat_loc)
  print len(dancoffByLoc.keys())
  print dancoffByLoc.keys()  

  makeDancoffMap(dancoffByLoc,arrayData)

  data = analyzeDancoffs(dancoffByLoc,arrayData,unitsWithFuel,dan_tolerance,skipped_lat_loc)
  arrayData = data[0]
  unitsWithFuel = data[1]

  makeDancoffMap(dancoffByLoc,arrayData)

  print 'EVERYTHING RAN!!!'



























if __name__ == '__main__':
  myProgram(sys.argv[1])
