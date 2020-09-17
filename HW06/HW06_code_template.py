# coding=UTF-8
import numpy as np

def search(pat, txt,q):
    lengthPattern = len(pat)
    lengthText = len(txt)

    p = 0
    t = 0

    for i in range(lengthPattern):
        p += (ord(pat[i])*pow(256,2))%q
        t += (ord(txt[i])*pow(256,2))%q

    print("Value for p: %d"%(p))
    for i in range(lengthText-lengthPattern+1):
        if(p==t):
            for j in range(lengthPattern):
                if(txt[i+j] != pat[j]):
                    break

            j+=1
            if(j == lengthPattern):
                print("Pattern found at index %d"%(i))
        
        if(i < lengthText-lengthPattern):
            t = t - int((ord(txt[i])*pow(256,2))%q) + int((ord(txt[i+lengthPattern])*pow(256,2))%q)
        print(txt[i])
        print(t)





if __name__ == "__main__":
    f = open('./06_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.core.defchararray.split(line, sep=",").tolist()
        search(npyArray[1], npyArray[0], int(npyArray[2]))
        

    f.close()



