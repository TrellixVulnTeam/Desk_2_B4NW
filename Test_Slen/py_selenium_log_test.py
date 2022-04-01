from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
url = "https://www.makemytrip.com/"
driver = webdriver.Chrome()
driver.get(url)


# @@ 1. Dynamic DropDown
# selenium.common.exceptions.ElementClickInterceptedException:
# Message: element click intercepted

# <input data-cy="fromCity" id="fromCity" type="text"
# class="fsw_inputField font30 lineHeight36 latoBlack" readonly="" value="Delhi">
# driver = webdriver.Chrome()

print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(1)

element = driver.find_element_by_id("fromCity")
# element = driver.find_element_by_xpath("//input[contains(@id, 'fromC')]")
# element = driver.find_element_by_xpath("//input[contains(@class, latoBlack)]")

e= driver.find_element_by_css_selector(input.fsw_inputField.font30)
# print(element.text)
time.sleep(2)
# element.click()