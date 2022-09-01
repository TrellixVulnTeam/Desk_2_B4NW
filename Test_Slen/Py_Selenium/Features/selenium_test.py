from selenium import webdriver
import time


opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")

prefs = {"profile.default_content_setting_values.notifications": 2}
opt.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=opt)

# @@ 2. Dynamic DropDown
# selenium.common.exceptions.ElementClickInterceptedException:
# Message: element click intercepted

# <input data-cy="fromCity" id="fromCity" type="text"
# class="fsw_inputField font30 lineHeight36 latoBlack" readonly="" value="Delhi">
# driver = webdriver.Chrome()
url = "https://www.makemytrip.com/"
driver.get(url)

print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(5)

element = driver.find_element_by_id("fromCity")
# element = driver.find_element_by_xpath("//input[contains(@id, 'fromC')]")
# element = driver.find_element_by_xpath("//input[contains(@class, latoBlack)]")

print(element.text)
time.sleep(2)
element.click()



#<input type="text" autocomplete="off" aria-autocomplete="list" aria-controls="react-autowhatever-1"
# class="react-autosuggest__input react-autosuggest__input--open" placeholder="From" value="">
css_selector = "input[placeholder='From']"
# from_field = driver.find_element_by_css_selector(css_sel)
# <p class="font14 appendBottom5 blackText">Bangkok, Thailand</p>
city_list = driver.find_elements_by_css_selector("p[class*='font14 appendBottom5 blackText']")
print(f"num of cities is {len(city_list)}")

# for i, city in enumerate(city_list):
#     print(i, city.text)
# num of cities is 20
# 0 Mumbai, India
# 1 Delhi, India
# 2 Bangkok, Thailand
# 3 Bangalore, India
# 4 Pune, India
# 5 Hyderabad, India
# 6 Kolkata, India
# 7 Chennai, India
# 8 Goa, India
# 9 Dubai, United Arab Emirates
# 10 Singapore, Singapore
# 11 Kathmandu, Nepal
# 12 Abu Dhabi, United Arab Emirates
# 13 Sharjah, United Arab Emirates
# 14 New York, US
# 15 London, United Kingdom
# 16 Hong Kong, Hong Kong
# 17 San Francisco, US
# 18 London, United Kingdom
# 19 Paris, France

# for i, city in enumerate(city_list):
#     if city.text  == "Bangkok, Thailand":
#         print(city.text) # Bangkok, Thailand
#         city.click()
#         time.sleep(2)
#         break


city_field = driver.find_element_by_css_selector(css_selector)
city_field.send_keys("bkk")
time.sleep(2)
# <p class="font14 appendBottom5 blackText">Bangkok, Thailand</p>
city_element = driver.find_element_by_xpath("//p[contains(text(),'Bangkok, Thailand')]")
city_element.click()

time.sleep(2)

destination = driver.find_element_by_xpath("//p[text()='Mumbai, India']")
print(destination.text) # Mumbai, India
time.sleep(2)
destination.click()
time.sleep(5)

print(driver.session_id)
# fc2e1bb0b59213ef134f86e9fff3a635

driver.close()



































