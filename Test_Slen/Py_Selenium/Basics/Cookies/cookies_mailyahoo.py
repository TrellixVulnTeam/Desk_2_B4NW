from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
url = "https://login.yahoo.com/?.intl=us&.lang=en-US&src=ym&done=https%3A%2F%2Fmail.yahoo.com%2Fd&add=1"
driver.get(url)
time.sleep(1)
print(driver.title) # Yahoo
print(driver.current_url)
driver.maximize_window()

candidate = "pice.bong@yahoo.com"
dd = "aA12345aA!"
# <input class="phone-no " type="text" name="username" id="login-username" tabindex="1"
# value="" autocomplete="username" autocapitalize="none" autocorrect="off" autofocus="true" placeholder=" ">

driver.find_element_by_css_selector("#login-username").send_keys(candidate)
time.sleep(1)
# <input id="login-signin" type="submit" name="signin" class="pure-button puree-button-primary challenge-button"
# value="Next" tabindex="6" data-rapid-tracking="true" data-ylk="elm:btn;elmt:primary;slk:next;mKey:login-landing-next"
# aria-hidden="false">

driver.find_element_by_xpath("//input[@name='signin']").click()
time.sleep(1)


# <input type="password" id="login-passwd" class="password" name="password"
# placeholder=" " autofocus="" autocomplete="current-password"
# data-rapid-tracking="true" data-ylk="elm:input;elmt:focus;slk:passwd;mKey:password-challenge-focus-passwd">

# <label for="login-passwd" id="password-label" class="password-label">Password</label>
driver.find_element_by_css_selector("#login-passwd").send_keys(dd)
# driver.find_element_by_css_selector("#password-label").send_keys(passwd)
# selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable


# <button type="submit" id="login-signin"
# class="pure-button puree-button-primary puree-spinner-button challenge-button"
# name="verifyPassword" value="Next" data-rapid-tracking="true" data-ylk="elm:btn;elmt:primary;slk:next;mKey:password-challenge-next">
#                     Next
#             </button>

next_button = driver.find_element_by_css_selector("button[name='verifyPassword']")
print("*************************************************")
print(next_button.get_attribute('innerHTML'))
# Next
print("-------------------------------------------------")
print(next_button.get_attribute('outerHTML'))
# <button type="submit" id="login-signin" class="pure-button puree-button-primary puree-spinner-button challenge-button" name="verifyPassword" value="Next" data-rapid-tracking="true" data-ylk="elm:btn;elmt:primary;slk:next;mKey:password-challenge-next">
#                     Next
#             </button>

with open("page_source1.html", "w", encoding='utf-8') as fout:
    fout.write(driver.page_source)

# print(type(driver.page_source)) # string
next_button.click()

cookies = driver.get_cookies()  # A list of cookies of type dict
i = 1
for dic in cookies:
    print(i, "************************")
    for k in dic:
        print(k,dic[k])
    i += 1

with open("cookies_file.txt", "w") as fout:
    for dic in cookies:
        fout.write(str(dic)+'\n')
driver.close()

time.sleep(10)
# url = "https://mail.yahoo.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.refresh()
time.sleep(10)
# load_cookie(driver)
for c in cookies:
    driver.add_cookie(c)
time.sleep(5)
driver.refresh()

print(driver.title)
print(driver.current_url)

# driver.close()

# selenium.common.exceptions.InvalidCookieDomainException: Message: invalid cookie domain: Cookie 'domain' mismatch
















































































