# https://rpaframework.org/libraries/browser_selenium/python.html
# https://robocorp.com/docs/development-guide/browser/how-to-switch-between-browser-windows
# https://robocorp.com/docs/development-guide/python/python-robot
# https://robotframework.org/SeleniumLibrary/SeleniumLibrary-5.0.0b1.html

from RPA.Browser.Selenium import Selenium
import time

browser = Selenium()

browser.open_available_browser("https://www.google.com")

# new window
browser.execute_javascript("window.open()")

handles = browser.get_window_handles()
print(handles)

# switch to new windows
browser.switch_window(handles[1])
# go to url
browser.go_to("https://www.yahoo.com")

time.sleep(2)
# switch to first window
browser.switch_window(handles[0])
time.sleep(2)
browser.switch_window(handles[1])
browser.close_window()
