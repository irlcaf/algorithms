# coding=UTF-8
import numpy as np

if __name__ == "__main__":
    f = open('./09_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.core.defchararray.split(line.rstrip(), sep=",").tolist()
        # Write your code here

    f.close()


