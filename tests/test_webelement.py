from source.finding_elements import *
import pytest
print("Execution starting ...")

# Scenario 1: Handling the Drop Down list
#url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
# add scenario execution lines here


# Scenario 2:
# variables
# call functions from finding_elements.py


@pytest.mark.smoke
@pytest.mark.checkbox
def test_checkbox(driver):
    print("# Scenario 2: Handling CheckBox")
    url_checkbox = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"
    open_website(url_checkbox)
    #create steps to test checkbox using selenium
    checkbox_test(driver)


@pytest.mark.dropdown
def test_drop_downdriver(driver):
    print("# Scenario 5: drop down list")
    drop_down_select(driver)

@pytest.mark.dropdown
def test_drop_down_multi_selct(driver):
    print("# Scenario 6: drop down multi select methods")
    drop_down_multi_select(driver)

@pytest.markswitchTo
def test_js_alerts(driver):
    print("# Scenario 7: handling the js alert")
    switch_to_alert(driver)

@pytest.mark.switchTo
def test_pop_up_window(driver):
    print("# Scenario 8: handling the popup window")
    switch_to_window(driver)

@pytest.mark.explicitWait
def test_explicit_wait(driver):
    print("Scenario 9: explicit wait cases")
    explicit_wait_methods(driver)


@pytest.mark.mouseMovements
def test_drag_drop(driver):
    print("Scenario 10: Mouse actions drag and drop")
    drag_drop_action3(driver)

@pytest.mark.mouseMovements
def test_mouse_move_element(driver):
    print("Scenario 11: mouse moving action- drag and drop")
    move_mouse_action(driver)


def test_close_bws(driver):
    print("closing the browser")
    close_browser(driver)
    print("Steps are completed!")