class Container:
    def __init__(self, id, customer, contractPrice):
        self.id = id
        self.x = -1
        self.y = -1
        self.z = -1
        self.customer = customer
        self.contractPrice = contractPrice

    def setcoord(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z





f= open("containers.txt", "r")
if f.mode == 'r':
    contents = f.read()

test = contents.split()

containers = []
size = len(test)/3

for i in range(size):
    id = test.pop(0)
    customer = test.pop(0)
    contractPrice = test.pop(0)
    containers.append(Container(id, customer, contractPrice))
