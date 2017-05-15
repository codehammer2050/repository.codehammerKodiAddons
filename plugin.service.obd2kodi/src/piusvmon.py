import piusv
import time
import os
from array import *


# Install:
#cp -r ~/downloads/piusv/* ~/.scripts/piusv


timeout = 20.0
curr_time = 0.0
piusv = piusv.PiUSV()
status = piusv.statusByte()
print(status)

# while 1:
while curr_time < timeout:
    if status[6] == 0:
        print('Ext USV Lost --> Running on Battery --> Shutting down System')
    curr_time = curr_time + .1
    #  os.system("shutdown now -h")
    print(curr_time)
    time.sleep(.1)
