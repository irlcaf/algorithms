# coding=UTF-8
import numpy as np

class maxHeap():
    def __init__(self, length):
        self.length = length
        self.Heap = [0]*(self.length)
        self.size = 0

    def parent(self,pos):
        return pos//2

    def leftChild(self,pos):
        return 2*pos +1

    def rightChild(self, pos):
        return 2*pos + 2

    def insert(self, element):
        self.Heap[self.size] = element
        self.size+=1


class PriorityQueue(object):
    def __init__(self, data):
        self.queue = data

    def isEmpty(self):
        return len(self.queue) == 0
    
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            self.queue = np.delete(self.queue, max)
        except IndexError:
            print()
            exit()
        return item

    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 


if __name__ == "__main__":
    f = open('./03_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line, dtype=int, sep=',')
        prio_queue = PriorityQueue(npyArray)
        n = np.array(0)

        #Getting the highest root
        n = np.append(n,prio_queue.delete())
        m = np.array(None)
        for i in range(0, len(prio_queue)):
            m = m.insert(node(n,prio_queue[(2*i)+1], prio_queue[(2*i)+2]))

        #print(prio_queue)
        #for i in range(0, len())
        #print(prio_queue.__str__())
        #print "The array representation of the heap is", npyArray
    f.close()



