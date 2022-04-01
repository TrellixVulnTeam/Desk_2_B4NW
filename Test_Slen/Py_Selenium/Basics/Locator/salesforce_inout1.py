from selenium import webdriver
from datetime import datetime
import time
from selenium.webdriver.common.by import By

url = "https://litepoint.my.salesforce.com/"
driver = webdriver.Chrome()
driver.get(url)

# <input class="input r4 wide mb16 mt8 username" type="email" value="" name="username"
# id="username" aria-describedby="error" style="display: block;">

username = driver.find_element("name","username").send_keys("jackChang")
# same as By.NAME
# username = driver.find_element(By.NAME,"username").send_keys("jackChang")



time.sleep(10)
driver.quit()

"""
selenium.webdriver.common.by
The By implementation.

class selenium.webdriver.common.by.By[source]
# Set of supported locator strategies.

CLASS_NAME = 'class name'¶
CSS_SELECTOR = 'css selector'
ID = 'id'
LINK_TEXT = 'link text'
NAME = 'name'
PARTIAL_LINK_TEXT = 'partial link text'
TAG_NAME = 'tag name'
XPATH = 'xpath'
"""