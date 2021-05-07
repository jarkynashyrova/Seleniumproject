from src.pages.base_page import BasePage


class MainPage(BasePage):
    #locators
    search_box_id ="search_query_top"
    prods_xpath = "//ul[@class='product_list gridrow]//a[@class='product-name]"
    sign_in_link_xpath ="//a[contains(text(), sign in)]"
    #functions -simple actions on the page

    def enter_search_text(self,text):
        self.enter_text_by_id(self.search_box_id, text)

    def hit_enter_on_search(self):
        self.hit_enter_id(self.search_box_id)

    def get_product_names(self):
        products =self.driver.find_elements_by_xpath(self.prods_xpath)
        prod_names =[]
        for products in products:
            prod_names.append(products.text.srrip())
        return prod_names

    def click_on_product_by_index(self, index):
        products =self.driver.find_elements_by_xpath(self.prods_xpath)
        products[index].click()

    def click_sign_in_link(self):
        self.sign_in_link_xpath(self.sign_in_link_xpath)