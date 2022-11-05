from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support       import expected_conditions as EC

url = "https://the-internet.herokuapp.com/windows"
driver = webdriver.Chrome(executable_path=r"C:\Users\jsun\Documents\Desk_2\libs\chromedriver.exe")
# time.sleep(1)
# driver.close()
driver.get(url)
# driver.maximize_window()
# <a href="/windows/new" ,="" target="_blank">Click Here</a>
print(driver.current_url)
print(driver.title)

# https://the-internet.herokuapp.com/windows
# The Internet
link_text = 'Click Here'
for i in range(1):
    driver.find_element_by_link_text(link_text).click()
    time.sleep(5)
    driver.close()
    # print(driver.current_window_handle)

# print(f"current URL is {driver.current_url}")
# # current URL is https://the-internet.herokuapp.com/windows

# there is no need to switch since diriver is still point to home page
# driver.switch_to.window(driver.current_window_handle)
# driver.switch_to.window(driver.window_handles[1])
# print(f"current tab's url is {driver.current_url}")
# current tab's url is https://the-internet.herokuapp.com/windows



time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
print(driver.current_url)
print(driver.title)

# https://the-internet.herokuapp.com/windows/new
# New Window
driver.get("https://yahoo.com")
time.sleep(3)
driver.close()
# driver.get("https://yahoo.com")

























































































