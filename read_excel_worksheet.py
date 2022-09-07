# https://rpaframework.org/libraries/excel_files/python.html
# https://robocorp.com/docs/development-guide/browser/rpa-form-challenge
from RPA.Excel.Files import Files

excel = Files()

excel.open_workbook("challenge.xlsx")
table = excel.read_worksheet_as_table(header=True)
excel.close_workbook()

print(table)

for person in table:
    print(person["First Name"] + " " + person["Last Name"])