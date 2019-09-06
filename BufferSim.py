from fsm import basicFSM
import numpy as np
fsm= basicFSM()
from random import *
darkRate_Hz = 10e3
darkPeriod_ns = 1.0/(darkRate_Hz*1e-9)
clockTick_ns = 16
darkProbPerPmtPerTick = clockTick_ns/darkPeriod_ns
numPmtsPerAsic = 4
print(darkProbPerPmtPerTick)

digitizeAndReadoutTime_ns = 24000
numWindows = 255
window_buffer=np.zeros((numWindows,), dtype=np.int)

timeNow_ns = 0
stopTime_ns = 1e9
queue = []

times   = []
lengths = []

lastLength = 0
step = 0
buffer_index_head = 0
buffer_index_tail = 0
buffer_digit_time = 0
queue_count = 0
event_count = 0
flag=0


print(fsm.current_state.value)
 
subBuffer = np.arange(0,2,1)

print(subBuffer)


def hits_gen():
    """
    Generate hits from the probability of a dark noise hit in the 1/2 of a window
    """
    if random() < darkProbPerPmtPerTick*numPmtsPerAsic:
       hit = True
       print(hit)
    else:
       hit= False
       print(hit)
    return hit

fsm.initial
fsm.current_state.value

numberSteps= stopTime_ns/clockTick_ns


for i in range(0,numberSteps, clockTick_ns):
    if hits_gen() = True:
         




print(totalTime)

