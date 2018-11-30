from container import Container
from stack import Stack
from customerReport import CustomerReport
import numpy as np


class Port:
    def __init__(self):
        # self.nextFreeRow = 0
        # self.movesLeft = 100
        # self.customerReports = []
        self.stacks = np.array([[Stack() for x in range(5)] for z in range(10)]) #10, 5 från början
    def addContainer(self, container):
        print(container.id)
        self.stacks[int(container.x)-1][int(container.z)-1].addContainerToStack(container)
    #def pcikup
