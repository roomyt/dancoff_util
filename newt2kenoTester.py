import sys
from stringSearch import findLineNum, findLineNumWithComments
from newt2keno import newt2keno
start = newt2keno(sys.argv[1])
#units = dancoffs.keys()
#for unit in units:
#  print unit,dancoffs[unit]['dancoffs'][92235]," @location ",dancoffs[unit]['location']
print start
