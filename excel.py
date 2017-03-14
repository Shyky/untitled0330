# -*- coding: UTF-8 -*-
from xlrd import open_workbook


class Arm(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return ("Arm object:\n"
                "  name = {0}\n"
                "  sex = {1}\n"
                "  age = {2}\n"
                .format(self.name, self.sex, self.age))


wb = open_workbook("test.xlsx")
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    print number_of_rows
    number_of_columns = sheet.ncols
    print number_of_columns

    items = []
    rows = []

    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value = sheet.cell(row, col).value
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        item = Arm(values)
        items.append(item)

for item in items:
    print item
    print("Accessing one single value (eg. DSPName): {0}".format(item.dsp_name))
