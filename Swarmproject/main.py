from container import Container
from stack import Stack
from customerReport import CustomerReport
from port import Port
import xlrd as xlrd
import numpy as np




def readFile(port, loc):
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    for j in range(sheet.nrows-1):
        row = j+1
        id = sheet.cell_value(row, 0)
        x = int(sheet.cell_value(row, 1))
        y = int(sheet.cell_value(row, 2))
        z = int(sheet.cell_value(row, 3))
        customer = sheet.cell_value(row, 4)
        contractPrice = sheet.cell_value(row, 7)
        businessValue = sheet.cell_value(row, 8)
        containerToAdd = Container(id, x, y, z, customer, contractPrice, businessValue)
        port.addContainer(containerToAdd)



loc = "sheet.xlsx"
port = Port()


readFile(port, loc)
port.getInQueue()
#port.getInQueue()

#port.findHighestValueInColumn(1)
