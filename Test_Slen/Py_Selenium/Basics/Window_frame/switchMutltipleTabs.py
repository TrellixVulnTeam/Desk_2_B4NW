from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support       import expected_conditions as EC

url = "https://the-internet.herokuapp.com/windows"
driver = webdriver.Chrome()
driver.get(url)
# driver.maximize_window()
# <a href="/windows/new" ,="" target="_blank">Click Here</a>

link_text = 'Click Here'
for i in range(4):
    driver.find_element_by_link_text(link_text).click()
    time.sleep(1)

# print(f"current URL is {driver.current_url}")
# # current URL is https://the-internet.herokuapp.com/windows

driver.switch_to.window(driver.current_window_handle)
print(f"current tab's url is {driver.current_url}")
# current tab's url is https://the-internet.herokuapp.com/windows



time.sleep(10)
driver.close()


























































































