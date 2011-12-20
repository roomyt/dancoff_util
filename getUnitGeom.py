#!/usr/bin/python -tt

import sys
import re
from stringSearch import findLineNum, string2list
from parseGeometryKeywords import parseGeometryKeywords

def getUnitGeom(lines):

  print 'Running getUnitGeom'

  unitGeom = {}   # This is the dictionary which will contain Geometry and Mixture info for the lattice

# Delete comments
  for line_num in range(len(lines)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if lines[line_num][0] == "'":
      del lines[line_num]         # delete the comments

# Find where the geometry block starts and ends
  start_geom = findLineNum(lines,'read geo')
  end_geom = findLineNum(lines,'end geo')

# Start interrogating each unit
  read_geom_unit = re.compile(r'(\d+)')
  for line_num in range(start_geom + 1, end_geom):
    if 'unit' not in lines[line_num]:
      continue
    else:
      unit = read_geom_unit.search(lines[line_num]).groups()
      unit = int(unit[0])
      end_of_unit = findLineNum(lines,'bound',start_index=line_num + 1)

      """ Now a unit which is in the lattice has been found and the lines 
          describing the unit are known section reads keywords(ie. cylinder,
          media) and makes a dictionary regionDict that stores info for each region.
          When all data for all regions is assembled, regionDict is added to dictionary 
          unitGeom for the appropriate unit.  
          - To process the unit geometry, the lines are split such that each
            word/number is an element in the list geomData"""
      unitGeom[unit] = parseGeometryKeywords(lines[line_num + 1: end_of_unit + 1], unit)
#  print unitGeom[100]
  return unitGeom


if __name__ == '__main__':
  f = open(sys.argv[1], 'r')  
  lines = f.read().split('\n')    # Read all lines
  for line_num in range(len(lines)-2,-1,-1):    # Stepping back through input, need -2 cuz extra empty spot at end of list assigned
    if lines[line_num][0] == "'":
      del lines[line_num]         # delete the comments
  getUnitGeom(lines)

