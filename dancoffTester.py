from getDancoff import *
dancoffs = getDancoff(sys.argv[1:])
units = dancoffs.keys()
for unit in units:
  print unit,dancoffs[unit]['dancoffs'][92235]," @location ",dancoffs[unit]['location']

