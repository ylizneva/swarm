from container import Container
from stack import Stack
from customerReport import CustomerReport
import numpy as np


class Port:
    def __init__(self):
        self.nextFreeRow = 0
        self.movesLeft = 100
        self.customerReports = []
        self.stacks = np.array([[Stack() for i in range(10)] for j in range(5)])

    def addContainer(self, container):
        print("larry")
