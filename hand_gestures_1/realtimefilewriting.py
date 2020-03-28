import numpy as np
import os
f = open("realtime.txt", "w")
arr = np.array([] , dtype=np.str)
i = 0
textList = ["One", "Two", "Three", "Four", "Five"]
while True:
    arr = np.append(arr, i)

    #np.savetxt('realtime.txt', [arr], fmt="%s")
    #np.loadtxt('realtime.txt')

    f.write('hello \n')

   #     os.fsync(f)
    i = i + 1

    if(i==100):
        f.flush()
        break

