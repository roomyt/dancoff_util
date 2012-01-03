import sys
import re
from getArrayData import getArrayData
from getUnitGeom import getUnitGeom
from stringSearch import findLineNum, findLineNumWithComments

def changeArray2KenoType(new_input,arrayData=0,unitGeom=0):
  """

  """
  print 'Running changeArray2KenoType'

  # Check if the dictionaries were given, if not then get them
  if arrayData == 0:
    arrayData = getArrayData(new_input)
  if unitGeom ==0:
    unitGeom = getUnitGeom

  # Find the lines describing the array block
  read_array = findLineNumWithComments(new_input,'read arr')
  end_array = findLineNumWithComments(new_input,'end arr',start_index=read_array)

  # This will be used to read the array number
  read_ara_num = re.compile(r'^ara\D*(\d*)\b')
  read_before_fill = re.compile(r'([a-zA-Z0-9,= ]*)fill')
  read_after_fill = re.compile(r'fill([a-zA-Z0-9,= ]*)')
  read_before_end = re.compile(r'([a-zA-Z0-9,= ]*)end')
  read_after_end = re.compile(r'end([a-zA-Z0-9,= ]*)')

  for line_num in range(read_array,end_array):
    if 'ara' in new_input[line_num]:
      array_num = int(read_ara_num.search(new_input[line_num]).groups()[0])
      if arrayData[array_num]['fuel_present'] == 'yes':
        nux = arrayData[array_num]['nux']
        nuy = arrayData[array_num]['nuy']

        # Isolate the part of the array definition that contains unit numbers
        # Make sure no numbers are on the same line as where 'fill' or 'end' are found
        start_fill = findLineNumWithComments(new_input,'fill',start_index=line_num)
        end_fill = findLineNumWithComments(new_input,'end',start_index=start_fill)
        start_fill_loc = new_input[start_fill].find('fill')
        end_fill_loc = new_input[end_fill].find('end')
        start_fill_text = new_input[start_fill]
        end_fill_text = new_input[end_fill]

        for line in new_input[start_fill:end_fill+6]:
          print line
        # Delete the lines that contain units
        del(new_input[start_fill:end_fill+1])

        # Insert a new line that contains everything including and after the word 'end' (preserve the 'end' keyword)
        new_input.insert(start_fill, read_after_end.search(end_fill_text).group() + '\n')
        # Replace the the where 'end' was found with all text before the word 'end' (isolate the unit numbers)
        new_input.insert(start_fill, read_before_fill.search(start_fill_text).group() + '\n')

        tmp_list = []
        for y in range(nuy):
          tmp_string = ''
          for x in range(nux):
            location = y*nux + x
            tmp_string = tmp_string + str(arrayData[array_num]['unitGivenLocation'][location]) + ' '
          tmp_string = tmp_string + '\n'
          tmp_list.append(tmp_string)

        for tmp_string in tmp_list:
          new_input.insert(start_fill+1,tmp_string)
        """ delete the lines that contain units
            make new string of units nux long, with nuy number of rows
            can use unitsByLocation (not these are newt location numbers)
            insert the new lines into new_input and add /n to each line
            """
#        for line in new_input[start_fill:end_fill+6]:
#          print line

  return new_input


if __name__ == '__main__':
 #   Read file, keeping the comments
    f = open(sys.argv[1], 'r')
    lines = f.read().split('\n')    # Read all lines
    f.close()
    changeArray2KenoType(lines)