from container import Container


class CustomerReport:
    def __init__(self, name):
        self.name = name
        self.containers = []
    def addContainer(self, container):
        self.containers.append(container)
    def invoice(self):
        totalPrice = 0
        for i in range(len(self.containers)):
            totalPrice = totalPrice + self.containers[i].contractPrice

        return totalPrice
