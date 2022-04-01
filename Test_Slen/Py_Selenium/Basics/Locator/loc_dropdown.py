from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

opts = webdriver.ChromeOptions()
opts.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(options=opts)
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(2)
#@@ 1. static drop down
# tag: select
#  provide methods to  handle options in drop-down menu

from selenium.webdriver.support.select import Select
# <select class="form-control" id="exampleFormControlSelect1">
#         <option>Male</option>
#         <option>Female</option>
# </select>
drop_down= driver.find_element_by_css_selector("select#exampleFormControlSelect1")
print(f"drop_down is {drop_down}")
# <selenium.webdriver.remote.webelement.WebElement
# (session="c16d0d074c7ff5b3622c7b902928144d",
# element="de98f9ef-73bb-4168-a0e1-171702e64ee4")>

dropdown1 = Select(drop_down)
print(dropdown1)
# <selenium.webdriver.support.select.Select object at 0x03620CF0>

# 1.1 select_by_visible_text
text = "Female"
dropdown1.select_by_visible_text(text)
# dropdown.select_by_value(value)

time.sleep(2)
driver.save_screenshot("dropdown_F.png")

# val = "Male"
# dropdown.select_by_value(val) # No value attribute
# driver.save_screenshot("dropdown_M.png")

# 1.2 select_by_index
dropdown1.select_by_index(0)
driver.save_screenshot("dropdown_M.png")
# time.sleep(10)
# dropdown.select_by_index(1)

# dropdown.deselect_by_visible_text()
# dropdown.deselect_all()
# driver.save_screenshot("dropdown_NO_select.png")
time.sleep(2)
# driver.quit()


driver.get(url)

print(f"drop_down is {drop_down}")
# drop_down is <selenium.webdriver.remote.webelement.WebElement (session="fb183a7419b56a8956c51d0fc6db6df6", element="d8dfe467-93dc-4fb1-86e2-bb3d5fad3ee9")>























































































