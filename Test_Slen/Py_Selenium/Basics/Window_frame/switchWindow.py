from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support       import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()

# <button id="openwindow" class="btn-style class1" onclick="openWindow()">Open Window</button>
loc_new_window= 'openwindow'
new_window= driver.find_element(By.ID, loc_new_window)
new_window.click()

driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
# http://www.qaclickacademy.com/
time.sleep(3)
driver.close()

driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)
# https://rahulshettyacademy.com/AutomationPractice/
time.sleep(2)
driver.close()

























































































