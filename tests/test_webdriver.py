from source.finding_elements import  *

print("Execution starting.....")
# scenario 1: Webdriver methods,properties,WbEelements ,ethod (input fields)
url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
open_website(url_inputs)
back_forward()
get_total_input_fields()

#scenario 2: Handling Checkbox
url_checkbox = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"
open_website(url_checkbox)
# create steps to test checkbox using selenium
checkbox_test()

#scenario 3: working with multiple elements, ecommerce website

# click on last product >  products[-1]
products[-1].click()
driver.refresh()