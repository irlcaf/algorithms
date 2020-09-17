# coding=UTF-8
import numpy as np

def flight_scheduling(newFlight, flightsScheduled, threshhold, numberFlights):

    if(newFlight + threshhold <= flightsScheduled[0] or newFlight - threshhold >= flightsScheduled[numberFlights]):
        print("Request at time %d is allowed."%(newFlight))
    else:
        for i in range(0, numberFlights):
            if(flightsScheduled[i] <= newFlight - threshhold and flightsScheduled[i+1] >= newFlight+ threshhold):
                print("Request at time %d is allowed."%(newFlight))
                return
        print("Request at time %d is not allowed"%(newFlight))
            

if __name__ == "__main__":
    f = open('./04_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line, dtype=int, sep=',')
        
        flightsScheduled = npyArray[1:npyArray[0]+1]
        threshhold = npyArray[npyArray[0]+1]
        newFlights = npyArray[-threshhold:]
        
        for i in range(len(newFlights)):
            flight_scheduling(newFlights[i], flightsScheduled, threshhold, len(flightsScheduled)-1)
            
        


    f.close()



