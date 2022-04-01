from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# from selenium import webdriver
# import time
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# opt = webdriver.ChromeOptions()
# # opt.add_argument('ignore-certificate-errors')

# Disable Chrome popup dialog
# opt.add_argument("--disable-notifications")

# # opt.add_argument('--allow-insecure-locolhost')
# # driver = webdriver.Chrome(options=opt)
# opt.add_argument("--disable-infobars")
#
# opt.add_argument("start-maximized")
#
# opt.add_argument("--disable-extensions")
#
# opt.add_experimental_option("prefs",
# {"profile.default_content_setting_values.notifications": 2
#  })

# opts.add_argument("headless")


# webElement = driver.find_element_by_id(locator)
# webElement actions
# send_keys("content"), click(), text,clear()
# get_attribute('attribute')

# driver actions
# driver.title
# driver.maximize_window()
# driver.minimize_window()
# driver.current_url
# driver.close() --> close current tab
# driver.quit()  --> close all tabs
# driver.refresh()
# driver.forward()
# driver.back()

# elem = driver.find_element_by_id()
# driver.find_element_by_class_name
# driver.find_element_by_name
# driver.find_element_by_xpath
# driver.find_element_by_css_selector
# driver.find_element_by_tag_name
# driver.find_element_by_link_text
# driver.find_element_by_partial_link_text

# driver.switch_to.active_element
# driver.switch_to.default_content()
# driver.switch_to.window()
# driver.switch_to.frame()
# driver.switch_to.alert

# browser
#1. FireFox
browser = webdriver.Firefox(executable_path = '/Users/zhaosong/Documents/WorkSpace/tool/geckodriver')
#2. Chrome
browser = webdriver.Chrome(executable_path = '/tool/chromedriver')
#. Internet Explorer
browser = webdriver.Ie("C:\\IEDriverServer.exe")
#Safari
browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
# Edge
edgeBrowser = webdriver.Edge(r"msedgedriver.exe")

#------------------------------------------------------
# 1. dynamic dropdown menu


# driver = webdriver.Firefox()
# url = "https://rahulshettyacademy.com/angularpractice/"
url = "https://www.makemytrip.com/"
driver.get(url)
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(2)
driver.close()











































































































