# https://rpaframework.org/libraries/browser_selenium/python.html
# https://robocorp.com/docs/development-guide/browser/how-to-switch-between-browser-windows
# https://robocorp.com/docs/development-guide/python/python-robot
# https://robotframework.org/SeleniumLibrary/SeleniumLibrary-5.0.0b1.html

from RPA.Browser.Selenium import Selenium
import time

browser = Selenium()

browser.open_available_browser("http://10.32.18.35:8080/inquire/SearchData.do?")


handles = browser.get_window_handles()
print(handles)



time.sleep(2)
# switch to first window
browser.switch_window(handles[0])
time.sleep(2)

browser.close_window()
