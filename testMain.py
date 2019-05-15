from random import *
import matplotlib.pyplot as plt
import numpy as np

darkRate_Hz = 10e3
darkPeriod_ns = 1.0/darkRate_Hz*1e9
clockTick_ns = 32
darkProbPerPmtPerTick = clockTick_ns/darkPeriod_ns
numPmtsPerAsic = 4

digitizeAndReadoutTime_ns = 24000
numWindows = 512
window_buffer=np.zeros((512,), dtype=np.int)

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
flag=0

plt.subplot(211)
plt.stem(window_buffer)
plt.subplot(212)
plt.plot(times, lengths)
plt.show()

while timeNow_ns < stopTime_ns and len(queue) < numWindows:
    if len(queue) > 0:
        queue[0] -= clockTick_ns
        
        if queue[0] <= 0:
            queue.pop(0)

    if random() < darkProbPerPmtPerTick*numPmtsPerAsic:
        queue.append(digitizeAndReadoutTime_ns)
        queue_count +=1
        
        if flag ==0 :
            buffer_digit_time = digitizeAndReadoutTime_ns
        window_buffer[buffer_index_head]+= 1
        flag =1
        if window_buffer[buffer_index_head] == 2:
            
            print("buffer full")
            print("time now:")
            print(timeNow_ns)
            print("buffer head:")
            print(buffer_index_head)
            print("buffer tail:")
            print(buffer_index_tail)
            print("queue count:")
            print(queue_count)

            plt.close()
            plt.subplot(211)
            plt.stem(window_buffer)
            plt.subplot(212)
            plt.plot(times, lengths)
            plt.show()
            break

        if buffer_index_head < 511:
            buffer_index_head +=1
        else:
            buffer_index_head=0

    if len(queue) != lastLength:
        times.append(timeNow_ns)
        lengths.append(len(queue))
    lastLength = len(queue)
    if step%1000000 == 0:
        print("time now:")
        print(timeNow_ns)
        print("buffer head:")
        print(buffer_index_head)
        print("buffer tail:")
        print(buffer_index_tail)

        plt.close()
        plt.subplot(211)
        plt.stem(window_buffer)
        plt.subplot(212)
        plt.plot(times, lengths)
        plt.show()
            
    timeNow_ns += clockTick_ns
    if queue_count > 0 :
        buffer_digit_time -= clockTick_ns
        
        if buffer_digit_time < 0 :
            window_buffer[buffer_index_tail]-=1
            queue_count -=1
            if buffer_index_tail < 511:
                buffer_index_tail+=1
            else :
                buffer_index_tail=0
            if queue_count > 0:
                buffer_digit_time=digitizeAndReadoutTime_ns
            else :
                flag =0

    step += 1

print("Sim End")
print("time now:")
print(timeNow_ns)
print("buffer head:")
print(buffer_index_head)
print("buffer tail:")
print(buffer_index_tail)

plt.clf
plt.subplot(211)
plt.stem(window_buffer)
plt.subplot(212)
plt.plot(times, lengths)
plt.show()