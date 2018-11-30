from container import Container


class Stack:
    def __init__(self):
        self.containerStack = []
    def isFull(self):
        #global isFull
        if len(self.containerStack) == 10:
            return True
        else:
            return False
    def addContainerToStack(self, container):
        if self.isFull() == False:
            #self.containerStack[int(container.y)-1] = container
            self.containerStack.append(container)
