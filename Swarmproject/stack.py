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
            print("test: ", container.z-1)
            self.containers[container.z-1] = container
            self.nrOf = self.nrOf + 1
    def getByZ(self, z):
        return self.containers[z-1]
