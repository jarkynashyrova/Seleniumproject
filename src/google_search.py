from time import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# steps
driver = webdriver.Chrome() #driver is onject class is Chrome
# or specify the path: driver = webdriver.Chrome('/path/to/chromedriver')
sleep(5) # hold

driver.get("https://google.com") # open

search_text_box = driver.find_element_by_name("q")
search_text_box.clear() # deleting evrything on search box
search_text_box.send_keys("python selenium integration")  # typing in the search box
search_text_box.send_keys(Keys.RETURN)  # hitting the enter key on keyboard
sleep(5)

search_text_box2 = driver.find_element_by_name("q")
search_text_box2.clear()  # delete everything in the search box
sleep(10)
driver.close()
print("completed!!!!!!!!!!!!!!!")

#scenario3

