from source.finding_elements import *
import pytest

print("Execution starting ...")

# @pytest.fixture()
# def browser():
    #implicit wait is defined once when you start the browser and this will apply all find element steps
    #this will disable ads , unwanted popups
    # options = Options()
    # options.add_argument('--disable-notifications')
    #options.add_argument('--headless')  # running the chrome on background
    #
    # driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(5)
    # driver.maximize_window()
    # return driver



@pytest.mark.sample
def test_sample_function():
    print("helo pytest")
    assert"hello" == "hello" # if it fails this will stop the execution
    print("completed.........")


@pytest.mark.smoke
@pytest.mark.webdriver
@pytest.mark.webdriver1
def test_webdriver_input_elements(driver):
    #print("Scenario 1: WebDriver methods, properties, WebElements methods (input fields)")
    url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
    # url_inputs = "https://www.google.com/" to generate pytest.fail status
    open_website(driver, url_inputs)
    back_forward(driver)

    get_total_input_fields(driver)

@pytest.mark.webdriver
@pytest.mark.ecommerce
@pytest.mark.skip
def test_ecommerce_products_example(driver):
    print("# Scenario 3 : working with multiple elements, ecommerce website")
    #go to this website and search the product
    print("scenario 3 started")
    website = "http://automationpractice.com/index.php"
    open_website(driver, website)
    ecommerce_search(driver)
    print("scenario 3 completed")


@pytest.mark.webdriver
@pytest.mark.amazon1
def test_amazon_example(driver):
    print("# Scenario 4: amazon example, find_elements")
    amazon_example(driver)
    assert driver.current_url == "https://www.amazon.com/"

