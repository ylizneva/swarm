from container import Container
from stack import Stack
from customerReport import CustomerReport
import numpy as np


class Port:
    def __init__(self):
        self.nextFreeRaw = 0
        self.movesLeft = 100
        self.customerReports = []
        self.stacks = np.array([[Stack() for i in xrange(10)] for j in xrange(10)])

    def addContainer(self, container):
        for i in range(10):
            if self.stacks[i, self.nextFreeRaw].isFull() == False:
                self.stacks[i, self.nextFreeRaw].addContainer(container)
