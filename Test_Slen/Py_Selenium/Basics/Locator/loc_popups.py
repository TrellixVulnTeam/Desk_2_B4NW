from selenium import webdriver
import time

# alert
# alert = driver.switch_to.alert
# alert.accept()
# javascript alert

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
print(driver.title)
print(driver.current_url)
# driver.maximize_window()
# driver.minimize_window()

## Switch To Alert Example
# @@ 4. popup
# <input id="name" name="enter-name" class="inputs" placeholder="Enter Your Name" type="text">
driver.find_element_by_css_selector("#name").send_keys("Alert Test Starts")
time.sleep(2)

# <input id="alertbtn" class="btn-style" value="Alert" onclick="displayAlert()" type="submit">
driver.find_element_by_id("alertbtn").click()

# driver.save_screenshot("alert.png") #  Selenium does NOT allow screenshot of alert
# selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: Hello Alert Test Starts,
# share this practice page and share your knowledge
# Message: unexpected alert open: {Alert text : Hello Alert Test Starts, share this practice page and share your knowledge}
time.sleep(2)

alert = driver.switch_to.alert
print(alert.text)
# Hello Alert Test Starts, share this practice page and share your knowledge
# alert.accept()
alert.dismiss()
driver.close()


aa="""
<fieldset class="pull-right">
                <legend>Switch To Alert Example</legend>
                <input id="name" name="enter-name" class="inputs" placeholder="Enter Your Name" type="text"><br>
                <input id="alertbtn" class="btn-style" value="Alert" onclick="displayAlert()" type="submit">
                <input id="confirmbtn" class="btn-style" value="Confirm" onclick="displayConfirm()" type="submit">
            </fieldset>
"""