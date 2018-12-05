from container import Container
from stack import Stack
from customerReport import CustomerReport
import numpy as np


class Port:
    def __init__(self):
        self.movesLeft = 100
        self.customerReports = []
        self.stacks = np.array([[Stack() for x in range(10)] for y in range(10)]) #Fixa så att 10 x 5 fungerar.

    def addContainer(self, container):
        self.stacks[container.x-1][container.y-1].addToStack(container)

    def getContainerAt(self, x, y, z):
        return self.stacks[x-1][y-1].getByZ(z)
    def getContainersOnTop(self, x, y, z):
        return self.stacks[x-1][y-1].above(z)
    def getHighestValueInStack(self, x, y):
        return self.stacks[x-1][y-1].getHighestContract()



    #def findHighestValueInColumn(self, column):
