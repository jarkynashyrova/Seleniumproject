from selenium import webdriver
from time import *
from selenium.webdriver.common.keys import Keys


# Study Group Tuesday April 27th

# find_element_by method
# Priority of methods:
# 1. id (guaranteed to be unique)
# 2. name
# 3. class name
# xpath, css_selector, tag name, link text, partial link text


driver = webdriver.Chrome()
url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(6)


# Scenario 1: get rid of pop-up commercial
driver.find_element_by_link_text("No, thanks!").click()


# Scenario 2: find some element by id (priority)
msg = driver.find_element_by_id("user-message")
msg.send_keys("Hello World")


# Scenario 3: use xpath
xpath = "//button[contains(text(),'Show Message')]"
driver.find_element_by_xpath(xpath).click()


# Scenario 4: find by id again
# enter a
driver.find_element_by_id("sum1").send_keys("7")
# enter b
driver.find_element_by_id("sum2").send_keys("7")


# Scenario 5: click on Get Total, xpath again
# Get Total
driver.find_element_by_xpath("//button[contains(text(),'Get Total')]").click()


# Scenario 6  ** Unresolved **
url2 = "https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html"
#driver.get(url2)
#driver.find_element_by_xpath("//button[@id='save']").click()


#sleep(3)
#FirstName = driver.find_element_by_xpath("//*[@id='loading']/text()[1]")
#LastName = driver.find_element_by_xpath("//*[@id='loading']/text()[2]")
#print(f"New user is: {FirstName}, {LastName} ")

# Next scenario, refresh a page
#print(f"New user is: {LastName}, {FirstName}")


#scenario 7 find element by name "q". google.com
url3 = "https://www.google.com/"
driver.get(url3)
search2 = driver.find_element_by_name("q")
search2.send_keys("mountains")
search2.send_keys(Keys.RETURN)