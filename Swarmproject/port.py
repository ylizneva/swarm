from container import Container
from stack import Stack
from customerReport import CustomerReport
import numpy as np


class Port:
    def __init__(self):
        self.movesLeft = 100
        self.customerReports = []
        self.stacks = np.array([[Stack() for x in range(10)] for y in range(10)]) #Fixa så att 10 x 5 fungerar.
        self.delList = []

    def addContainer(self, container):
        self.stacks[container.x-1][container.y-1].addToStack(container)

    def getContainerAt(self, x, y, z):
        return self.stacks[x-1][y-1].getByZ(z)
    def getContainersOnTop(self, x, y, z):
        return self.stacks[x-1][y-1].above(z)
    def getHighestValueInStack(self, x, y):
        return self.stacks[x-1][y-1].getHighestContract()

    def getInQueue(self):
        for j in range(100):
            biggest = 0
            biggestContainer = self.stacks[0][0].getTop()
            containerX = 0
            containerY = 0
            for y in range(10):
                for x in range(10):
                    container = self.stacks[x][y].getTop()
                    #print("x: ",x+1, "y:", y+1)
                    #print(container.id)
                    if container.id != 'null' and self.stacks[x][y].getTop().planned == False and container != -1:
                        #print(biggest, container.contractPrice)
                        if (container.contractPrice>biggest):
                            biggest=container.contractPrice
                            biggestContainer = container
                            containerX = x
                            containerY = y
                            #print(biggest)
            self.stacks[containerX][containerY].getTop().planned = True
            self.delList.append(biggestContainer)
            #print("Biggest", biggestContainer.id)


        for i in range (len(self.delList)):
            print("List ", self.delList[i].contractPrice, self.delList[i].z)

        #print("isPlanned: ", self.stacks[containerX][containerY].getTop().planned)





    #def findHighestValueInColumn(self, column):
