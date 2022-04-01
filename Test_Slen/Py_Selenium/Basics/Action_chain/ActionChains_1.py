from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ActionChains
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
url = "https://www.familysearch.org/"
driver.get(url)
driver.implicitly_wait(2)

#
# Search
#
# </button>
element = driver.find_element(By.XPATH, "//button[text()='Search']")
print(element.get_attribute("outerHTML"))
action_item = action.move_to_element(element)
# action_item.click().perform()
# element.click()

# <a href="/search/family-trees" class="submenu-link"
# data-config="lo_hdr9_srch:genealogies"
# data-test="genealogies"
# data-component-init="AdobeLinkTracker">
#
# Genealogies
#
# </a>

genealogies_button = driver.find_element(By.LINK_TEXT, 'Genealogies')
# genealogies_button.click()

action_item.click().perform().move_to_element(genealogies_button).click().perform()

# action_item.perform()
# <a href="/search/family-trees" class="sub-menu-link" data-config="lo_hdr_srch:genealogies" data-test="genealogies"
# data-component-init="AdobeLinkTracker">Genealogies</a>
# action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()

# <h1 class="grande fs-h3">Search Genealogies</h1>

# text_ver = driver.find_element_by_xpath("//h1[text()='Search Genealogies']").text # working
# text_ver = driver.find_element(By.XPATH, "//div[@class='search-purpose']/h1").text
# text_ver = driver.find_element(By.CSS_SELECTOR, "div[class='search-purpose'] h1").text
# print(text_ver) # Search Genealogies


# ex1
#
# driver = webdriver.Firefox(executable_path="")
# driver.get("https://UrlToOpen")
#
# action = ActionChains(driver)
#
# firstLevelMenu = driver.find_element_by_id("menu")
# action.move_to_element(firstLevelMenu).perform()
# secondLevelMenu = driver.find_element_by_xpath("//a[contains(text(),'menu1')]")
# action.move_to_element(secondLevelMenu).perform()
# secondLevelMenu.click()
#
#
#
#
#
# time.sleep(3)
# driver.close()


#鼠标悬停的

# 1. 定义鼠标悬停的元素：
move = driver.find_element_by_css_selector(
    'div.queryschema-control.ivu-col.ivu-col-span-16 > div > div > div > input')
# 2.模拟鼠标悬停：
ActionChains(driver).move_to_element(move).perform()

# 3.操作悬停后出现的元素
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()