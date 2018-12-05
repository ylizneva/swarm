from container import Container
import numpy as np


class Stack:
    def __init__(self):
        self.containers = np.empty(10, dtype=object)
        self.nrOf = 0
    def isFull(self):
        if self.nrOf == 10:
            return True
        else:
            return False
    def addToStack(self, container):
        if self.isFull() == False:
            self.containers[container.z-1] = container
            self.nrOf = self.nrOf + 1
    def getByZ(self, z):
        return self.containers[z-1]
    def above(self, z):
        containersTop = self.nrOf - z
        return containersTop
    def getHighestContract(self):
        highestValue = self.containers[0]
        #print(highestValue.contractPrice - self.above(highestValue.z))
        #print(self.containers[1].contractPrice - self.above(self.containers[1].z))
        print((highestValue.contractPrice - self.above(highestValue.z)))
        for i in range(self.nrOf):
            if self.containers[i].contractPrice != 'null':
                print(self.containers[i].contractPrice)
                if(highestValue.contractPrice - self.above(highestValue.z))<(self.containers[i].contractPrice - self.above(self.containers[i].z)):
                    highestValue = self.containers[i]
        return highestValue
