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

    def findHighestValueInColumn(self, column): #kolumen, vågrätt. Mellan 1-10
        highestValue = self.stacks[0][column].getByZ(1)
        print(highestValue.id)
        for i in range(10):
            for k in range(5):
                print(self.stacks[i][column].getByZ(k).id)
                if highestValue.contractPrice < self.stacks[i][column].getByZ(k).contractPrice:
                    highestValue = self.stacks[i][column].getByZ(k)
        return highestValue
