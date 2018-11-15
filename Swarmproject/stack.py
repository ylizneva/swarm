from container import Container


class Stack:
    def __init__(self):
        self.containers = []
    def isFull(self):
        #global isFull
        if len(self.containers) == 5:
            return True
        else:
            return False
    def addContainer(self, container):
        if self.isFull() == False:
            self.containers.append(container)
