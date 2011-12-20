import sys

def makeDancoffMap(dancoffByLoc,arrayData):
  for array in arrayData:
    if arrayData[array]['fuel_present'] == 'yes':
      nuy = arrayData[array]['nuy']
      nux = arrayData[array]['nux']
      print ' '
      print ' Location Map '
      for y in range(0,nuy):
        string = ''
        for x in range(0,nux):
          loc = x + y*nux
          string = string + ' ' + str(loc)
        print string

      print ' '
      print ' DanMap '
      for y in range(0,nuy):
        string = ''
        for x in range(0,nux):
          loc = x + y*nux
          if loc not in dancoffByLoc.keys():
            string = string + '    None    '
          else:
            string = string + ' ' + str(dancoffByLoc[loc]['dancoffs'][92235])
        print string

      print ' '
      print ' Unit Map '
      for y in range(0,nuy):
        string = ''
        for x in range(0,nux):
          loc = x + y*nux
          string = string + ' ' + str(arrayData[array]['unitGivenLocation'][loc])
        print string
