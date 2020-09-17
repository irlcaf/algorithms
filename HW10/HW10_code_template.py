# coding=UTF-8
import numpy as np

if __name__ == "__main__":
    f = open('./10_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line.rstrip(), dtype=int, sep=',')
        # Write your code here

    f.close()

