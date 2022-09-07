# https://robocorp.com/portal/robot/robocorp/example-html-table-robot
# https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files
import time
from html_tables import *
from RPA.Browser.Selenium import Selenium
from RPA.Tables import Tables

browse = Selenium()
tables = Tables()

browse.open_available_browser("https://www.w3schools.com/html/html_tables.asp", headless=True)
html_table = browse.get_element_attribute("css:table#customers", "outerHTML")
print(html_table)

table = read_table_from_html(html_table)
dimensions = tables.get_table_dimensions(table)
first_row = tables.get_table_row(table,0)
first_cell = tables.get_table_cell(table,0,0)
for row in table:
    print(row)
print()
print(first_row)
print()
print(first_cell)

