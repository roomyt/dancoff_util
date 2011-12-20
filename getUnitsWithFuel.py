import sys
import re
from stringSearch import findLineNum
from getFuelMixtures import getFuelMixtures

def getUnitsWithFuel(lines,fuelMixtures=0):

  print 'Running getUnitsWithFuel'

  if fuelMixtures == 0:
    fuelMixtures = getFuelMixtures(lines)

  unitsWithFuel = []   # List of units that contain fuel material

  for line_num in range(len(lines)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if lines[line_num][0] == "'":
      del lines[line_num] 

  read_geom = findLineNum(lines,'read geom')
  end_geom = findLineNum(lines,'end geom',start_index=read_geom)

  read_unit = re.compile(r'unit\D+(\d+)')
  read_media = re.compile(r'media\D+(\d+)')

  for line in lines[read_geom + 1 : end_geom]:
    if line.find('unit') != -1:
      unit_num = int(read_unit.search(line).groups()[0])
    elif line.find('media') != -1:
      mixtureID = int(read_media.search(line).groups()[0])
#      print mixtureID
      if mixtureID in fuelMixtures:
#        print 'mixtureID = ', mixtureID
        if unit_num not in unitsWithFuel:
#          print 'unit = ', unit_num
          unitsWithFuel.append(unit_num)
    else:
      continue
#  print unitsWithFuel
  return unitsWithFuel
    

if __name__ == '__main__':
  f = open(sys.argv[1], 'r')  
  lines = f.read().split('\n')    # Read all lines
  getUnitsWithFuel(lines)
