
import math
file=open('./01_input.in','r')

def frequency(file_n):
    list = {}
    for lines in file_n:
        line = lines.split()
        if line is not None:    
            for item in line:
                item_c = item.lower().rstrip(",.-")
                if item_c in list:
                    list[item_c] += 1
                else:
                    list[item_c] = 1
    return list

def vectorizing(freq_1, freq_2):
    vector_1 = []
    vector_2 = []
    for words in freq_1:
        if words in freq_2:
            vector_1.append(freq_1.get(words))
            vector_2.append(freq_2.get(words))
        else:
            vector_1.append(freq_1.get(words))
            vector_2.append(0)
    for words in freq_2:
        if words not in freq_1:
            vector_1.append(0)
            vector_2.append(freq_2.get(words))
    return [vector_1, vector_2]

def dot(a,b): 
    return sum( [a[i]*b[i] for i in range(len(b))] )

def cosine_similarity(a,b):
    return float(dot(a,b) / ((math.sqrt(dot(a,a))) * (math.sqrt(dot(b,b)))))

while True:
    filename_1 = file.readline().rstrip()
    filename_2 = file.readline().rstrip()

    if not filename_1 or not filename_2:
        break

    file_1 = open(filename_1,'r')
    file_2 = open(filename_2,'r')

    [vector_1, vector_2] = vectorizing(frequency(file_1), frequency(file_2))

    print(cosine_similarity(vector_1, vector_2))
    
    file_1.close()
    file_2.close()

file.close()

    
    



