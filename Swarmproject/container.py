class Container:
    def __init__(self, id, customer, contractPrice, businessValue):
        self.id = id
        self.x = -1
        self.y = -1
        self.z = -1
        self.customer = customer
        self.contractPrice = contractPrice
        self.businessValue = businessValue

    def setcoord(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
