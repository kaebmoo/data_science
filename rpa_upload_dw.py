import time
# from RPA.Browser.Selenium import Selenium
from RPA.Windows import Windows

# lib = Selenium()
library = Windows()

# เปิดโปรแกรมเครื่องคิดเลข
library.windows_run("calc.exe")

# เปิด script เพื่อ upload ข้อมูลขึ้น data warehouse
library.windows_run("C:\\Users\\CAT\\Documents\\GitHub\\bot\\upload_dw.bat")

