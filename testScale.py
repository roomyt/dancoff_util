import sys
import os
import subprocess
from stringSearch import findLineNum, findLineNumWithComments


args = "'" + 'scale6' + ' ' + sys.argv[1] + "'"
print args

subprocess.Popen([args])

#scale6 (sys.argv[1])

print 'done'
