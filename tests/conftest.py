import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from utilities import *


@pytest.fixture(scope='module')
def driver():
    print("\************** I am a set up****************")
    #implicit wait is defined once when you start the browser and this will apply all find element steps
    #this will disable ads , unwanted popups
    print("initializing the browser.......")
    options = Options()
    options.add_argument('--disable-notifications')
    #options.add_argument('--headless')  # running the chrome on background

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()

    #return driver # this  is not needed if you are using yield
    yield driver

    print("\n************** I am a TEARDOWN**************")
    print("closing the browser...........")
    img1 = f'screenshots/{get_str_seconds()}_completed.png'
    driver.get_screenshot_as_file(img1)
    driver.quit()
