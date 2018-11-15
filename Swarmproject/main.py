from container import Container
from stack import Stack
from customerReport import CustomerReport


container1 = Container(1, "Ikea", 30)
container2 = Container(2, "Bha", 1)
container3 = Container(3, "Amazon", 34)
container4 = Container(4, "Ikea", 8)
container5 = Container(5, "Bla", 20)

stack = Stack(1,2)

customer = CustomerReport("Ikea")
customer.addContainer(container1)
customer.addContainer(container2)
customer.addContainer(container3)
customer.addContainer(container4)

print(customer.containers[1].contractPrice)

print(customer.invoice())
