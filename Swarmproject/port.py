from container import Container
from stack import Stack
from customerReport import CustomerReport
import numpy as np


class Port:
    def __init__(self):
        self.movesLeft = 100
        self.customerReports = []
        self.stacks = np.array([[Stack() for x in range(10)] for y in range(10)])
        self.delList = []
        self.lista =[]
        self.anotherLista =[]

    def addContainer(self, container):
        self.stacks[container.x-1][container.y-1].addToStack(container)

    def getContainerAt(self, x, y, z):
        return self.stacks[x-1][y-1].getByZ(z)
    def getContainersOnTop(self, x, y, z):
        return self.stacks[x-1][y-1].above(z)

    def getInQueue(self):
        #print(self.stacks[0][0].getSum()
        sum = self.stacks[0][0].getSum()
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
                            #print(biggest)1q   q

                self.stacks[containerX][containerY].getTop().planned = True
                self.delList.append(biggestContainer) #spara en dyraste container i en lista

    def sumPrices(self):
        sum = 0
        for i in range(10):
            for j in range(10):
                sum = self.stacks[i][j].getSum() + sum
        return sum

    def nrOfCont(self):
        sum = 0
        for i in range(10):
            for j in range(10):
                sum = self.stacks[i][j].getNrOf() + sum
        return sum

    def oneMoveCost(self):
        move = 0
        move = (self.sumPrices()/self.nrOfCont())/self.movesLeft #Ska oneMoveCost ändras hela tiden eller ska den vara samma?
        return move

    def moveQuality(self):
        containersprice = 0
        bla = 0
        print(self.getContainerAt(1, 1, 1).id)
        for i in range(10):
            for j in range(10):
                for q in range(5):
                    containersOnTop = self.getContainersOnTop(i+1, j+1, q+1)#hur många som står ovanpå
                    self.lista.append(containersOnTop+1) #antal moves som krävs för att flytta container, inkl containern själv
                    container = self.getContainerAt(i+1, j+1, q+1)
                    if container.id != 'null':
                        if i+1 != container.x or j+1 != container.y or q+1 != container.z: #kollar så att index och kordinater är samma
                            print("container kord och index kord stämmer inte")
                            return
                        print("Längd: ", len(self.lista))
                        print("ID: ", container.id)
                        print("Moves to get to:  ", self.lista[-1])
                        print("Contract price: ", container.contractPrice)
                        containersprice = self.lista[-1]*self.oneMoveCost()
                        print("move*0.067 = ", containersprice)
                        #print("Contractprice - moveWorth:", container.contractPrice - containersprice)

                        #self.anotherLista.append(

                        #print("Worth: ", len(self.anotherLista))
