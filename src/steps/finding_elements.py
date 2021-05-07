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
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from src.pages.main_page import MainPage
from utilities import *




def open_website(driver,url):
    """open the website, and click on 'No, thanks!' button"""
    try:
        driver.get(url)
        print(f"Title of the page 1: {driver.title}")

        # time.sleep(10)  # one way of holding the execution and to wait for something
        wdwait = WebDriverWait(driver, 10)
        wdwait.until(EC.visibility_of_element_located((By.ID, "site-name")))

        print("now clicking the 'No thanks' button..")
        driver.find_element_by_link_text('No, thanks!').click()
    except (WebDriverException, NoSuchElementException, TimeoutException) as err:
        print(f"Unable to to open website correctly.\n {err}")
        pytest.fail("unable to open website correctly.")


def back_forward(driver):
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


def get_total_input_fields(driver):
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


def close_browser(driver):
    driver.close()  # close the current tab
    driver.quit()  # closes the browser


def checkbox_test(driver):
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


def ecommerce_search(driver):
    # find the element by id 'search_query_top'
    # search for dress (hit enter or click on search button)
    main_page = MainPage(driver)

    main_page.enter_search_text('dress')

    #srch_box = driver.find_element_by_id("search_query_top")
    #srch_box.send_keys("dress")
    #srch_box.send_keys(Keys.RETURN)
    #time.sleep(5)
    main_page.hit_enter_on_search()
    # get the list of products and get the text out of each product
    #     use find elements to find products listed, this returns a list named 'products'
    #     loop through this list and use element.text
    # check the count of products
    print(main_page.get_product_names())
    main_page.click_on_produc_by_index(-1)
    main_page.click_sign_in_link()
    driver.refresh()

    #     we have a list of elements, len(products)
    #print(f"we have {len(products)} products listed.")
    # click on last product >  products[-1]
    #products[-1].click()
    driver.refresh()


def amazon_example(driver):
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


def drop_down_select(driver):
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


def drop_down_multi_select(driver):
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


def switch_to_alert(driver):
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


def switch_to_window(driver):
    driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")

    print(" ***** switching to window *************")
    email_locator = '//input[@name="session[username_or_email]"]'
    url_window_popup = "https://www.seleniumeasy.com/test/window-popup-modal-demo.html"
    twt_xpath = '//a[@title="Follow @seleniumeasy on Twitter"]'

    driver.get(url_window_popup)
    print(f"This is the unique id of current tab/window: {driver.current_window_handle}")
    # 'CDwindow-A2808C3F2699449C54C66AD5CC9238D0'
    main_window = driver.current_window_handle  # we are saving this unique ID so we can come back to this window
    driver.find_element_by_xpath(twt_xpath).click()  # this opens a new window
    print(f"listing all unique id of all windows open: {driver.window_handles}")
    # ['CDwindow-A2808C3F2699449C54C66AD5CC9238D0', 'CDwindow-76A031EDBFB5279E9CA44EBEEFD9AB24']
    handles = driver.window_handles  # we can save in all ids in the list
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


def explicit_wait_methods(driver):
    # Variables and objects
    url = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"
    # click button:  #populate-text
    # explictitly wait until
    # text_to_be_present_in_element(locator,text_) -- "Selenium"
    # locators: h2 (id), //h2[@id='h2'] (xpath), #h2 (css selector)
    # driver.find_element_by_xpath("//h2[@id='h2' and text()='Selenium Webdriver']") -- this is not good
    msg_xpath = "//h2[@id='h2']"
    msg_id = "h2"
    msg_css_selector = "#h2"
    # locator1 = (By.XPATH, msg_xpath)
    extd_txt = "Selenium Webdriver"
    wdwait = WebDriverWait(driver, 60)

    # Steps starts here
    driver.get(url)

    print("## Case 1: text_to_be_present_in_element")
    element = driver.find_element_by_id("populate-text")  # finding the button to click
    # printing the message of the h2 before clicking
    msg_txt = driver.find_element_by_xpath(msg_xpath)
    print(f"Current message text: {msg_txt.text}")
    element.click()

    print("waiting until expected text to appear ...")
    # WebDriverWait(driver, 60).until(expected_conditions.text_to_be_present_in_element((By.XPATH, msg_xpath), extd_txt))
    msg = wdwait.until(EC.text_to_be_present_in_element((By.XPATH, msg_xpath), extd_txt))
    print(f"did message appear now? - {msg}")
    print(f"New (expected) message text: {msg_txt.text}")

    print("## Case 2: visibility_of_element_located")
    display_btn_id = "display-other-button"
    driver.find_element_by_id(display_btn_id).click()
    print("waiting until enabled button appears...")
    enabled_btn = wdwait.until(EC.visibility_of_element_located((By.ID, 'hidden')))
    enabled_btn.click()
    print("waiting until enabled button disappears...")
    wdwait.until_not(EC.visibility_of_element_located((By.ID, 'hidden')))
    print("case 2 completed!")

    print("## Case 3: element_to_be_clickable")
    enabled_btn_id = "enable-button"
    driver.find_element_by_id(enabled_btn_id).click()
    print("waiting until Button button is clickable...")
    wdwait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#disable')))
    print("case 3 completed!")

    print("## Case 4: element_to_be_clickable")
    check_btn_id = "checkbox"
    driver.find_element_by_id(check_btn_id).click()
    print("waiting until box is selected...")
    wdwait.until(EC.element_to_be_selected((By.CSS_SELECTOR, '#ch'))) # this return True/False
    driver.find_element_by_css_selector("#ch").click()
    print("waiting until box is unchecked...")
    wdwait.until_not(EC.element_to_be_selected((By.CSS_SELECTOR, '#ch')))
    print("case 4 completed!")


def drag_drop_action(driver):
    """
    Demonstrates to handle drag and drop mouse movements with Selenium.
    """
    pass
    url = "https://www.seleniumeasy.com/test/drag-and-drop-demo.html"
    driver.get(url)

    print("Identifying the steps and target elements...")
    elem1 = driver.find_element_by_xpath("//span[contains(text(),'Draggable 1')]")
    elem2 = driver.find_element_by_xpath("//span[contains(text(),'Draggable 2')]")
    elem3 = driver.find_element_by_xpath("//span[contains(text(),'Draggable 3')]")
    elem4 = driver.find_element_by_xpath("//span[contains(text(),'Draggable 4')]")

    drop_area = driver.find_element_by_xpath("//div[@id='mydropzone']")

    print("performing the drag and drop action")
    actions = ActionChains(driver)
    actions.drag_and_drop(elem1, drop_area).pause(1).perform()
    # actions.drag_and_drop_by_offset(elem1, 150, 0).perform()
    time.sleep(10)
    print("completed drag and drop.")


def drag_drop_action2(driver):
    """
    Demonstrates to handle drag and drop mouse movements with Selenium.
    """
    url = "https://www.globalsqa.com/demo-site/draganddrop/"
    driver.get(url)
    time.sleep(5)

    print("Identifying the steps and target elements...")
    elem1 = driver.find_element_by_xpath("//img[contains(@src, 'high_tatras_min.jpg')]")
    elem2 = driver.find_element_by_xpath("//img[contains(@src, 'high_tatras_min2.jpg')]")
    elem3 = driver.find_element_by_xpath("//img[contains(@src, 'high_tatras_min3.jpg')]")
    elem4 = driver.find_element_by_xpath("//img[contains(@src, 'high_tatras_min4.jpg')]")

    drop_area = driver.find_element_by_xpath("//div[@id='trash']")

    print("performing the drag and drop action")
    actions = ActionChains(driver)
    actions.drag_and_drop(elem1, drop_area).perform()
    time.sleep(10)
    print("completed drag and drop.")


def drag_drop_action3(driver):
    # Step:
    # start the website
    # drag and drop item 1
    # verify item 1 is under dropped list
    # drag and drop item 2
    # verify item 2 is under dropped list

    driver.get("http://testautomationpractice.blogspot.com/")
    item1 = driver.find_element_by_xpath("//div[@id='draggable']")
    drop_zone = driver.find_element_by_xpath("//div[@id='droppable']")

    actions = ActionChains(driver)
    actions.drag_and_drop(item1, drop_zone).perform()
    # actions.move_to_element(item1, drop_zone).perform() # hover over element (mouse movement)
    time.sleep(10)
    print("drag and drop finished.")


def move_mouse_action(driver):
    driver.get("http://automationpractice.com/index.php")

    time.sleep(5)
    prod_xpath = '//ul[@id="homefeatured"]//a[@title="Faded Short Sleeve T-shirts" and @class="product-name"]'

    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(5)
    prod1 = driver.find_element_by_xpath(prod_xpath)

    actions = ActionChains(driver)
    actions.move_to_element(prod1)
    # actions.drag_and_drop_by_offset(prod1, 300, 150)
    time.sleep(10)














