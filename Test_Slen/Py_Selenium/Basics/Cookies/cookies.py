
from selenium import webdriver
import time
driver = webdriver.Chrome()

# driver.add_cookie(cookie_dictionary)
#
# driver.delete_cookie(cookie_name)
# driver.delete_all_cookies()
#
# driver.get_cookie(cookie_name)
# driver.get_cookies()


# Navigate to url
driver.get("http://www.example.com")

# Adds the cookie into current browser context
driver.add_cookie({"name": "foo", "value": "bar"})
# driver.add_cookie({"name": "test", "value": "QA"})
cookie = driver.get_cookies()
print(cookie)

driver.add_cookie({"name": "test", "value": "QA"})
# driver.delete_cookie("name")
# driver.delete_all_cookies()
cookie = driver.get_cookies()
print(cookie)


time.sleep(1000)
# Get cookie details with named cookie 'foo'
print(type(driver.get_cookies()))
print(driver.get_cookies())
# <class 'list'>
# [{'domain': 'www.example.com', 'httpOnly': False, 'name': 'foo', 'path': '/', 'secure': False, 'value': 'bar'}]

# Get cookie details with named cookie 'foo'
print(driver.get_cookie("foo"))
print(type(driver.get_cookie("foo")))

# <class 'dict'>
# {'domain': 'www.example.com', 'httpOnly': False, 'name': 'foo', 'path': '/', 'secure': False, 'value': 'bar'}

# Delete a cookie with name 'foo'
driver.delete_cookie("foo")

print(driver.get_cookies())
# [{'domain': 'www.example.com', 'httpOnly': False, 'name': 'test', 'path': '/', 'secure': False, 'value': 'QA'}]

#  Deletes all cookies
driver.delete_all_cookies()

print(driver.get_cookies()) # []

print(driver.get_cookie("foo"))  # None