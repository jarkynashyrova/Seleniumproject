# Finding the elements:
# by name,
# by id (fastest if the element ID is unique),
# by class name,
# by link text, by partial link text

# by xpath (customizable, flexible, element hierarchy can be used better),
# by css selector (customizable, flexible),

# Functions from selenium
# find_element_by_id(id)

# start the browser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utilities import *

# implicit wait is defined once when you start the browser and this will apply all find element steps
# this will disable ads , unwanted popups
options = Options()
options.add_argument('--disable-notifications')
options.add_argument('--headless')  # running the chrome on background

driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(5)
driver.maximize_window()


def open_website(url):
    """open the website, and click on 'No, thanks!' button"""
    try:
        driver.get(url)
        print(f"Title of the page 1: {driver.title}")

        # time.sleep(10)  # one way of holding the execution and to wait for something
        print("now clicking the 'No thanks' button..")
        driver.find_element_by_link_text('No, thanks!').click()
    except NoSuchElementException as err:
        print(f"pop did not appear this time.\n {err}")


def back_forward():
    img1 = f'./../screenshots/{get_str_seconds()}_datapage.png'
    img2 = f'./../screenshots/{get_str_seconds()}_seleniumdemo.png'

    driver.back()
    time.sleep(5)
    print(f"Title of the page 2: {driver.title}")
    driver.get_screenshot_as_file(img1)

    driver.forward()
    print(f"Title of the page 3: {driver.title}")
    driver.get_screenshot_as_file(img2)
    time.sleep(5)


def get_total_input_fields():
    """
    find the "Enter a" input box
    find the "Enter b" input box
    enter the "20" text in a
    enter the "30" text in b
    """
    img1 = f'./../screenshots/{get_str_seconds()}_result.png'

    driver.find_element_by_id('sum1').send_keys("20")
    bvalue_input = driver.find_element_by_id('sum2')
    bvalue_input.send_keys("30")

    # find the "Get Total" button, then click on that button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sum_button = driver.find_element_by_xpath("//button[text()='Get Total']")
    # sum_button = driver.find_element_by_class_name("btn btn-default")
    # sum_button = driver.find_element_by_link_text("Get Total")
    sum_button.click()
    driver.get_screenshot_as_file(img1)


def close_browser():
    driver.close()  # close the current tab
    driver.quit()  # closes the browser


def checkbox_test():
    # todo: code here
    # find the element (using xpath) to check, and click
    check_xpath = "//input[@id='isAgeSelected']"

    print("checkbox test started ...")
    checkbox = driver.find_element_by_xpath(check_xpath)
    checkbox.click()
    time.sleep(5)

    # verify the checkbox is checked
    print(f"Is Checkbox selected (True/False): {checkbox.is_selected()}")

    # find the message element and get text
    msg_css_selector = "#txtAge"
    msg = driver.find_element_by_css_selector(msg_css_selector)
    msg_text = msg.text
    print(f"Final message: {msg_text}")

    assert "Success" in msg_text


def ecommerce_search():
    # find the element by id 'search_query_top'
    # search for dress (hit enter or click on search button)

    srch_box = driver.find_element_by_id("search_query_top")
    srch_box.send_keys("dress")
    srch_box.send_keys(Keys.RETURN)
    time.sleep(5)

    # get the list of products and get the text out of each product
    #     use find elements to find products listed, this returns a list named 'products'
    #     loop through this list and use element.text
    # check the count of products
    prods_xpath = "//ul[@class='product_list grid row']//a[@class='product-name']"
    products = driver.find_elements_by_xpath(prods_xpath)  # list
    prod_names = []
    for product in products:
        prod_names.append(product.text.strip())

    #     we have a list of elements, len(products)
    print(f"we have {len(products)} products listed.")
    # click on last product >  products[-1]
    products[-1].click()
    driver.refresh()


def amazon_example():
    """
    demonstrates some methods from WebDriver Class.
    (current_url, driver.title, driver.clear,
    """
    # driver = webdriver.Chrome()
    host = "https://www.amazon.com/"
    driver.get(host)
    host = driver.current_url  # this will return the current page url

    print(host)  # 'https://www.amazon.com/'
    if driver.current_url == host:
        print("yess test passed")
    else:
        print("noo test failed")

    print(f"Title of the current page: {driver.title}")
    'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more'
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys("kids toys")

    search_box.send_keys(Keys.RETURN)
    search_box.clear()


def drop_down_select():
    url_dropdown = "https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html"
    driver.get(url_dropdown)
    driver.refresh()
    ddown_list = driver.find_element_by_id("select-demo")  # Select element
    selection = Select(ddown_list)  # object to represent your drop down on UI
    print("Different ways of selecting from drop down list: ")
    selection.select_by_visible_text('Tuesday')
    selection.select_by_index(5)
    selection.select_by_value("Monday")

    print("options method: returns list of options in the drop down")
    for element in selection.options:
        print(element.text)

    print("first_selected_option: returns element select")
    print(selection.first_selected_option.text)
    print("all_selected_options: returns list of selected option(s):")
    for element in selection.all_selected_options:
        print(element.text)


def drop_down_multi_select():
    url_dropdown = "https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html"
    driver.get(url_dropdown)
    ddown_list = driver.find_element_by_id("multi-select")  # Select element with '<select>' tag
    selection = Select(ddown_list)

    # Multi select drop down enables you to select multi options
    selection.select_by_value("New York")
    selection.select_by_visible_text("Ohio")
    print("selection.all_selected_options :")
    for element in selection.all_selected_options:
        print(element.text)  # this will return all selected options (new york, ohio)
    print("Delesecting by index: ")
    selection.deselect_by_index(4)

    selection.select_by_index(5)
    selection.select_by_index(7)
    print("Deselecting_all : ")
    selection.deselect_all()


def switch_to_alert():
    driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
    driver.find_element_by_xpath("//button[@onclick='myAlertFunction()']").click()
    alert = driver.switch_to.alert
    print(alert.text)  # 'I am an alert box!'
    print("Clicking the OK button")
    alert.accept()
    print("***** handling alerts with multiple buttons *** ")
    driver.find_element_by_xpath("//button[@onclick='myPromptFunction()']").click()
    alert2 = driver.switch_to.alert
    alert2.send_keys("John Doe")
    alert2.send_keys("John Doe")

    print("Clicking the CANCEL button")
    alert2.dismiss()
    driver.find_element_by_xpath("//button[@onclick='myPromptFunction()']").click()
    alert2.send_keys("John Doe")
    print(alert2.text)  # 'Please enter your name'
    alert2.accept()


def switch_to_window():
    driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")

    print(" ***** switching to window *************")
    email_locator = '//input[@name="session[username_or_email]"]'
    url_window_popup = "https://www.seleniumeasy.com/test/window-popup-modal-demo.html"
    twt_xpath = '//a[@title="Follow @seleniumeasy on Twitter"]'

    driver.get(url_window_popup)
    print(f"This is the unique id of current tab/window: {driver.current_window_handle}")
    # 'CDwindow-A2808C3F2699449C54C66AD5CC9238D0'
    main_window = driver.current_window_handle # we are saving this unique ID so we can come back to this window
    driver.find_element_by_xpath(twt_xpath).click() # this opens a new window
    print(f"listing all unique id of all windows open: {driver.window_handles}")
    # ['CDwindow-A2808C3F2699449C54C66AD5CC9238D0', 'CDwindow-76A031EDBFB5279E9CA44EBEEFD9AB24']
    handles = driver.window_handles # we can save in all ids in the list
    print("switching to the second window, this will be second element from the handles list.")
    driver.switch_to.window(handles[1])

    print("finding the email input and entering the email on the second window.")
    email_input = driver.find_element_by_xpath(email_locator)
    email_input.send_keys("myawesomeemail@gmail.com")

    print("switching the focus back to main window")
    driver.switch_to.window(handles[0])
    print("switching the focus to second window, twitter window.")
    driver.switch_to.window(handles[1])
    email_input = driver.find_element_by_xpath(email_locator)
    email_input.send_keys("a")
    email_input.send_keys(Keys.TAB)
    email_input.send_keys("bb")
    email_input.send_keys(Keys.TAB)
    email_input.send_keys(Keys.TAB)
    print('switching the window is completed.')

def
    url ="https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"
    element = driver.find_element_by_id("popultae-text")
    msg_xpath ="//h2[@id='h2]"']
    msg_id = "h2"
    msg_css_selector ="h2"
    #locator1 = (By.XPATH, msg_xpath)

    extd_txt = "Selenium Webdriver"
    wedwait = WebDriverWait(driver, 60)

    wdwait.until.(EC.text_to_be_present_in_element(By.XPATH),extd_txt)
