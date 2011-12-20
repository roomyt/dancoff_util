import sys
from operator import itemgetter
from random import randint

def analyzeDancoffs(dancoffByLoc,arrayData,unitsWithFuel,dan_tolerance,skipped_lat_loc):
  dancoffByUnit = {}   # {unit : [(dancoff1, location1), (dancoff2, location2), etc] }
  originalUnitGivenNewUnit = {}    # {NewUnitNum : OriginalUnitNum}
  """new_units is a dictionary that contains lists with info [old_unit_num, [lattice_positions]]
     for each position that has a significantly different Dancoff factor than similar units.
     Where [lattice_positions] is a list of all lattice_positions that will use this new unit definition.
  """
  print arrayData[1].keys()
  print unitsWithFuel
  for array in arrayData:
    if arrayData[array]['fuel_present'] == 'yes':
      for unit in arrayData[array]['units_list']:
        if unit in unitsWithFuel:
          locations = arrayData[array]['locationsGivenUnit'][unit]
          danList = []
          print dancoffByLoc
          print skipped_lat_loc
          for location in locations:
            if location == 19:
              print 'here'
            print location
            if location in skipped_lat_loc:
                dan = 0.0000
            else:
                dan = float(dancoffByLoc[location]['dancoffs'][92235])
# may need to add logic for Gd dancoffs here
            temp_tuple = (dan,location)
            danList.append(temp_tuple)
          # For each unit, the locations are sorted by dancoff from least to greatest
          danList.sort(key=itemgetter(0))
          dancoffByUnit[unit] = danList
      print dancoffByUnit

      # Examine each unit in the array
      # Needed to use this while loop logic because the number of units keeps changing but Python only evaluated it at the beginning
      done = 'F'
      unit_count = -1
      units_to_be_analyzed = dancoffByUnit.keys()  # list of units
      while done == 'F':
        unit_count = unit_count + 1   # unit_count is used as the indice for units below (# units can grow as they split by dancoff)
        unit = units_to_be_analyzed[unit_count]
        # Use average Dancoff for a unit as criteria for making new units
        # Iterate through each location for similar dancoffs
        sum_dan = 0.0
#debug
        print len(dancoffByUnit[unit]), 'NUMBER OF DANCOFFS IN UNIT ', unit
        num = -1   # num is the indice for a dancoff factor of a fuel pin within the unit (multiple fuel pins assigned to each unit)
        while num < (len(dancoffByUnit[unit]) - 1):
          num = num + 1
          print 'num is ', num
          print 'unit is ', unit
          print dancoffByUnit[unit]
          sum_dan = sum_dan + dancoffByUnit[unit][num][0]
          ave_dan = sum_dan/float(num + 1.0)
          diff_dan = ave_dan - dancoffByUnit[unit][num][0]
          # Check for a significant difference in Dancoff from the running average
          if abs(diff_dan) > dan_tolerance*ave_dan:
            print 'Greater than ',dan_tolerance*100,'% difference in Dancoff at location ', \
                   dancoffByUnit[unit][num][1], ' compared to average Dancoff for unit ',unit
            # Generate new unit number and check if it is used already
            new_unit = unit
            while new_unit in arrayData[array]['units_list']:
              new_unit = randint(1,200)
#debug
            print 'NEW UNIT NUMBER IS ', new_unit
            print ' '
            # Append the new_unit to dancoffByUnit, just take a slice of the original one
            dancoffByUnit[new_unit] = dancoffByUnit[unit][num:]
            # Replace the list of tuples with the shortened list (only locations with similar dancoffs)
            dancoffByUnit[unit] = dancoffByUnit[unit][0:num]
            # Make a dictionary of new units and related original units, make sure the "original" unit actually is original
            if unit in originalUnitGivenNewUnit.keys():
              originalUnitGivenNewUnit[new_unit] = originalUnitGivenNewUnit[unit]
            else:
              originalUnitGivenNewUnit[new_unit] = unit
            # Add this new unit to the list of units to be analyzed
            units_to_be_analyzed.append(new_unit)
            # Update some of the dictionaries with the new unit (others will be updated later)
            unitsWithFuel.append(new_unit)
            arrayData[array]['units_list'].append(new_unit)
            # Every Dancoff in this unit is now within the tolerance of their average
            # Go to the next unit
            print 'ABOUT TO BREAK'
        # Check if there are anymore units
        if unit_count + 1 == len(dancoffByUnit.keys()):
          done = 'T'

      print "I'm updating dictionaries"
      """ Update other dictionaries and lists with new unit data"""
      print dancoffByUnit   #debugging
      for unit in dancoffByUnit.keys():
        for num in range(len(dancoffByUnit[unit])):
          location = dancoffByUnit[unit][num][1]
          arrayData[array]['unitGivenLocation'][location] = unit

      for num in range(len(arrayData[array]['units_list'])):
        tmp_list = []
        if arrayData[array]['units_list'][num] in arrayData[array]['locationsGivenUnit']:
          continue
        else:
          tmp_list.append(num)
          for num2 in range(num + 1, len(arrayData[array]['units_list'])):
            if arrayData[array]['units_list'][num] == arrayData[array]['units_list'][num2]:
              tmp_list.append(num2)
          arrayData[array]['locationsGivenUnit'][arrayData[array]['units_list'][num]] = tmp_list

      arrayData[array]['originalUnitGivenNewUnit'] = originalUnitGivenNewUnit
      arrayData[array]['dancoffByUnit'] = dancoffByUnit
  

#debug
  print 'DANCOFF BY UNIT '
  print dancoffByUnit

  data = [arrayData, unitsWithFuel]
  return data





      
