from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Hide / Show message
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice"
driver.get(url)
driver.minimize_window()


# <input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">
    #shadow-root (user-agent)
#       <div pseudo="-webkit-input-placeholder" id="placeholder" style="display: block !important;">Hide/Show Example</div>
#       <div></div>
# HTML within shadow-root can not be located by selenium, js can help
# hide_text = driver.find_element_by_name("show-hide")
xpath1="//*[@name='show-hide']"
host_element = driver.find_element(By.XPATH, xpath1)

js = "return document.getElementById('displayed-text').shadowRoot"
loc = driver.execute_script(js)
loc = loc.find_element_by_id("placeholder")
print(loc.text)








# assert driver.find_element_by_id('displayed-text').is_displayed()
#
# # <input id="hide-textbox" class="btn-style class2" value="Hide" onclick="hideElement()" type="submit">
# driver.find_element_by_id('hide-textbox').click()
#
# assert not driver.find_element_by_id('displayed-text').is_displayed()
#
# time.sleep(5)
# # <input id="show-textbox" class="btn-style class2" value="Show" onclick="showElement()" type="submit">
# driver.find_element_by_css_selector('#show-textbox').click()
# time.sleep(10000)







# driver.close()


























































































