# coding=UTF-8
import numpy as np

if __name__ == "__main__":
    f = open('./02_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line, dtype=int, sep=',')
        peak = 0
        for i, item in enumerate(npyArray):
            if(i == 0):
                if(npyArray[0] > npyArray[1]):
                    peak = npyArray[0]
            elif(i == len(npyArray)-1):
                if(npyArray[len(npyArray)-2] < npyArray[len(npyArray)-1]):
                    peak = npyArray[len(npyArray)-1]
            else:
                if(npyArray[i] > npyArray[i-1] and npyArray[i] > npyArray[i+1]):
                    peak = npyArray[i]
        print("Find it! Peak element is %d"%peak)


        # Write your code here

    f.close()
