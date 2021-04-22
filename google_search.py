from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # or webdriver.Chrome('/path/to/chromedriver')

driver.get("https://google.com")

search_text_box = driver.find_element(By.NAME, "q")
search_text_box.clear()
search_text_box.send_keys("python selenium integration")
search_text_box.send_keys(Keys.RETURN)



