# import time
#
# from selenium.common import StaleElementReferenceException
# from selenium.webdriver.common.by import By
# from pages.BasePage import BasePage
# from constants.ui_constants import Titles, Messages
#
# class AllProductsPage(BasePage):
#     div_allProducts_xpath = (By.XPATH,"//div[@class='features_items']")
#     txt_search_id = (By.ID,"search_product")
#     btn_searchSubmit_id = (By.ID,"submit_search")
#     txt_searchedProd_xpath = (By.XPATH,"//div[@class='features_items']/h2[text()='Searched Products']")
#     lnk_cart_xpath = (By.XPATH,"//a[text()=' Cart']")
#
#
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#
#     def validatePageTitle(self):
#         actual_title = self.driver.title
#         assert actual_title == Titles.PRODUCTS, f"Expected Products Page Title is: {Titles.PRODUCTS} and the Actual Products Page Title is: {actual_title}"
#
#
#     def validateAllProducts(self):
#         try:
#             #assert self.validateElement(*self.div_allProducts_xpath),"All Products section not found"
#             assert self.validateMsg(self.div_allProducts_xpath), "All Products section not found"
#         except Exception as e:
#                 print("The error is: ", e)
#
#     # def searchProduct(self,product):
#     #     try:
#     #         self.inputText(self.txt_search_id,product)
#     #         self.clickElement(self.btn_searchSubmit_id)
#     #
#     #     except Exception as e:
#     #             print("The error is: ", e)
#
#     def searchProduct(self, product):
#
#         self.inputText(
#
#             self.txt_search_id,
#
#             product
#
#         )
#
#         self.clickElement(
#
#             self.btn_searchSubmit_id
#
#         )
#
#         return self
#
#     def validateSearchedProd(self):
#         assert self.validateMsg(self.txt_searchedProd_xpath),"Searched Products section not found"
#
#
#         # Locators
#         # This selects the 'Price' tag inside every product block
#     ALL_PRICES = (By.XPATH, "//div[@class='productinfo text-center']/h2")
#     CONTINUE_SHOPPING = (By.XPATH, "//button[text()='Continue Shopping']")
#
#
#     def add_products_above_price(self, threshold):
#         """
#                    Finds all products on the page, checks their price,
#                    and adds them to cart if Price > threshold.
#                    """
#         price_elements = self.getElements(self.ALL_PRICES)
#
#         # 1. Get all price elements
#         #price_elements = self.getElements(self.ALL_PRICES)
#
#         for price_element in price_elements:
#             # Convert text "Rs. 500" -> integer 500
#             price_text = price_element.text  # e.g., "Rs. 500"
#             numeric_price = int(price_text.replace("Rs. ", "").strip())
#
#             if numeric_price > threshold:
#             # Dynamic XPath relative to the price we just found
#             # Move up to the container, then down to the specific 'Add to Cart' button
#                  add_to_cart_xpath = f"./following-sibling::a"
#
#                 # Scroll to it to avoid 'ElementClickIntercepted'
#                  self.driver.execute_script("arguments[0].scrollIntoView();", price_element)
#
#                 # Click the button belonging to this specific price
#                  price_element.find_element(By.XPATH, add_to_cart_xpath).click()
#
#                  # Wait for modal and close it
#                  self.clickElement(self.CONTINUE_SHOPPING)
#                  print(f"Added product with price: {numeric_price}")
#         # #self.clickElement(self.lnk_viewCart_xpath)
#
#     def clickOnCart(self):
#         self.clickElement(self.lnk_cart_xpath)
#

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from constants.ui_constants import Titles

class AllProductsPage(BasePage):
    div_allProducts_xpath = (By.XPATH,"//div[@class='features_items']")
    txt_search_id = (By.ID,"search_product")
    btn_searchSubmit_id = (By.ID,"submit_search")
    txt_searchedProd_xpath = (By.XPATH,"//div[@class='features_items']/h2[text()='Searched Products']")
    lnk_cart_xpath = (By.XPATH,"//a[text()=' Cart']")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def validatePageTitle(self):
        actual_title = self.driver.title
        assert actual_title == Titles.PRODUCTS, f"Expected Products Page Title is: {Titles.PRODUCTS} and the Actual Products Page Title is: {actual_title}"


    def validateAllProducts(self):
        try:
            #assert self.validateElement(*self.div_allProducts_xpath),"All Products section not found"
            assert self.validateMsg(self.div_allProducts_xpath), "All Products section not found"
        except Exception as e:
                print("The error is: ", e)

    # def searchProduct(self,product):
    #     try:
    #         self.inputText(self.txt_search_id,product)
    #         self.clickElement(self.btn_searchSubmit_id)
    #
    #     except Exception as e:
    #             print("The error is: ", e)

    def searchProduct(self, product):

        self.inputText(self.txt_search_id,product)

        self.clickElement(self.btn_searchSubmit_id)

        return self

    def validateSearchedProd(self):
        assert self.validateMsg(self.txt_searchedProd_xpath),"Searched Products section not found"


        # Locators
        # This selects the 'Price' tag inside every product block
    ALL_PRICES = (By.XPATH, "//div[@class='productinfo text-center']/h2")
    CONTINUE_SHOPPING = (By.XPATH, "//button[text()='Continue Shopping']")


    def add_products_above_price(self, threshold):
        """
                   Finds all products on the page, checks their price,
                   and adds them to cart if Price > threshold.
                   """
        price_elements = self.getElements(self.ALL_PRICES)

        # 1. Get all price elements
        #price_elements = self.getElements(self.ALL_PRICES)

        for price_element in price_elements:
            # Convert text "Rs. 500" -> integer 500
            price_text = price_element.text  # e.g., "Rs. 500"
            numeric_price = int(price_text.replace("Rs. ", "").strip())

            if numeric_price > threshold:
            # Dynamic XPath relative to the price we just found
            # Move up to the container, then down to the specific 'Add to Cart' button
                 add_to_cart_xpath = f"./following-sibling::a"

                # Scroll to it to avoid 'ElementClickIntercepted'
                 self.driver.execute_script("arguments[0].scrollIntoView();", price_element)

                # Click the button belonging to this specific price
                 price_element.find_element(By.XPATH, add_to_cart_xpath).click()

                 # Wait for modal and close it
                 self.clickElement(self.CONTINUE_SHOPPING)
                 print(f"Added product with price: {numeric_price}")
        # #self.clickElement(self.lnk_viewCart_xpath)

    def clickOnCart(self):
        self.clickElement(self.lnk_cart_xpath)

