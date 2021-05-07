from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, diver):
        self.driver = driver
        self.bdwait =WebDriverWait(driver, 60)

    def click_element_by_id(self,id):
        element = self.driver.find_element_by_id(id)
        element.click()

    def click_element_by_xpath(self, xpath):
        element = self.wdwait.until(EC.element_to_be_clickable(By.XPATH, xpath)))
        element.click()

    def enter_text_by_id(self, id, text):
        element = self.wdwait.until(EC.presence_of_element_located(By.id, id)))
        element.send.keys(text)
        time.sleep(2)

    def enter_text_by_id(self, xpath, text):
        element = self.wdwait.until(EC.presence_of_element_located(By.XPATH, xpath)))
        element.send.keys(text)
        time.sleep(2)

    def hit_enter(self):
        element = self.wdwait.until(EC.presence_of_element_located(By.id, id)))
        search for dress (hit enter or click on search button)