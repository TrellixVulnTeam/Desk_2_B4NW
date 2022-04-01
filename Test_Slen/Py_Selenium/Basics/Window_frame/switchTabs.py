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
driver.find_element_by_link_text(link_text).click()

new_tab = driver.window_handles[1]
driver.switch_to.window(new_tab)
print(f"new_tab url is {driver.current_url}")
# new_tab url is https://the-internet.herokuapp.com/windows/new
print(driver.find_element_by_tag_name("h3").text)

assert driver.find_element(By.XPATH, "//h3[text()='New Window']").text == "New Window"
driver.close()

time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
print(f"current url is {driver.current_url}")
# current url is https://the-internet.herokuapp.com/windows
assert driver.find_element_by_tag_name("h3").text == "Opening a new window"


time.sleep(3)
driver.close()


























































































