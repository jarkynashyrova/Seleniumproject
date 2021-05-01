from source.finding_elements import *
import pytest


print("Execution starting ...")

@pytest.mark.webdriver1
def test_webdriver_input_elements():
    print("Scenario 1: WebDriver methods, properties, WebElements methods (input fields)")
    url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
    open_website(url_inputs)
    back_forward()
    get_total_input_fields()

def test_checkbox():
    print("# Scenario 2: Handling CheckBox")
    url_checkbox = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"
    open_website(url_checkbox)
    #create steps to test checkbox using selenium
    checkbox_test()

def tes_ecommerce_product_example():
    print("# Scenario 3 : working with multiple elements, ecommerce website")
    #go to this website and search the product
    print("scenario 3 started")
    website = "http://automationpractice.com/index.php"
    #open_website(website)
    #ecommerce_search()
    print("scenario 3 completed")

def tes_amazon():
    print("# Scenario 4: amazon example, find_elements")
    amazon_example()

def tes_drop_down():
    #print("# Scenario 5: drop down list")
    drop_down_select()

def test_drop_down_multi():
    #print("# Scenario 6: drop down multi select methods")
    drop_down_multi_select()

def test_js_alerts():
    print("# Scenario 7: handling the js alert")
    switch_to_alert()

def test_pop_up_window():
    print("# Scenario 8: handling the popup window")
    switch_to_window()

def test_explicit_wait():
    print("Scenario 9: explicit wait cases")
    explicit_wait_methods()

def close():
    print("closing the browser")
    close_browser()
    print("Steps are completed!")

def test_drag_drop():
    print("closing the browser")
    drag_drop_action()
    drag_drop_action()
    drag_drop_action3()

def test_closing_browser():
    print("closing the window")
    close_browser()



def test_mouse_move_element():
    print("Scenario 11: mouse moving action")
    move_mouse_action()

def test_close_bws():
    print("closing the browser")
    close_browser()
    print("Steps are completed!")







