from container import Container
from stack import Stack
from customerReport import CustomerReport
from port import Port
import xlrd as xlrd




def readFile(port, loc):
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    print(sheet.nrows)

    for j in range(sheet.nrows-1):
        row = j+1
        id = sheet.cell_value(row, 0)
        x = sheet.cell_value(row, 1)
        y = sheet.cell_value(row, 2)
        z = sheet.cell_value(row, 3)
        customer = sheet.cell_value(row, 4)
        contractPrice = sheet.cell_value(row, 7)
        businessValue = sheet.cell_value(row, 8)
        print(id, x, y, z, customer, contractPrice, businessValue)
        print(1)










loc = "sheet.xlsx"
port = Port()

readFile(port, loc)
