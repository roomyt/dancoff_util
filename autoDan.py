import sys
import re
from stringSearch import findLineNum, findLineNumWithComments, string2list
from subprocess import Popen
from SPyT.Utilities.utils import *  # Used to get scale directory path

def autoDan(filename):

# Remove Excessive spaces
  blanks = re.compile(r'[ ]{4,}')
  for line_num in range(len(lines)):
    lines[line_num] = re.sub('[ ]{4,}',' ', lines[line_num])

# Edit the input so that parm=check
  read_comp = findLineNumWithComments(lines,'read comp')
  get_sequence = re.compile(r'=\s*(\S+)\b')
  tmp_line_num = 0
  for line_num in range(read_comp):
    sequence_line = findLineNumWithComments(lines,'=',start_index=tmp_line_num)
    sequence = get_sequence.search(lines[sequence_line]).groups()[0]
    if 'shell' in sequence:
      tmp_line_num = sequence_line
      continue
    else:
      break
  print sequence

# Check for parm, then add check if not there.
  if lines[sequence_line].find('parm') == -1:
    lines[sequence_line] = lines[sequence_line] + ' parm=check \n'
  else:
    

#  for line_num in range(read_comp):
#    new_input[line_num] = "'/" + new_input[line_num]

#  new_input.insert(0, "'batch_args \-m \n")
#  new_input.insert(0, 'ce_v7_endf \n')
#  new_input.insert(0, 'KENO input converted from NEWT \n')
#  new_input.insert(0, '=csas6 parm=check \n')

  return new_input
  
# Find the scale_path and version
  scale_path = get_scale_root()
  find_version = re.compile(r'scale(\d+.\d+)')
  version = find_version.search(scale_path).groups()[0]

# Setup the arguments needed to run Scale
  args = []
  if '/' in scale_path:
    machine = posix
    args.append(scale_path + '/cmds/batch' + version)
  else:
    machine = windows
    args.append(scale_path + '\cmds\batch' + version + '.bat')
  args.append(' -m ')
  args.append(new_filename)
  Popen(args)








if __name__ == '__main__':
  f = open(sys.argv[1], 'r')  
  lines = f.read().split('\n')    # Read all lines
  f.close()
  autoDan(lines)
