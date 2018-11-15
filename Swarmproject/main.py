from container import Container
from stack import Stack
from customerReport import CustomerReport
from port import Port


container1 = Container(1, "Ikea", 30)
container2 = Container(2, "Bha", 1)
container3 = Container(3, "Amazon", 34)
container4 = Container(4, "Ikea", 8)
container5 = Container(5, "Bla", 20)

port = Port()
port.addContainer(container1)
port.addContainer(container2)
port.addContainer(container3)
port.addContainer(container4)
port.addContainer(container5)
print(port.stacks[0,0].containers[1].customer)
