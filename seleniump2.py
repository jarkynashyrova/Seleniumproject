from selenium import webdriver
from time import *
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "https://www.amazon.com/"
driver.get(url)

driver.maximize_window()
driver.implicitly_wait(6)

search1 = driver.find_element_by_name("field-keywords")
search1.send_keys("alexa")
search1.send_keys(Keys.RETURN)