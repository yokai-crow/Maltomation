'''
A) command to try and fix corrupted or modified system files.

B) Target the running Operating System Perform cleanup
   and recovery operations on the running Operating System'''

import os
A = 'SFC/SCANNOW'
B = 'DISM.exe/Online/Cleanup-Image/Restorehealth'

os.system(A)
os.system(B)