import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


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
        try:
            #self.waitForElement((By.XPATH,self.txt_Account_xpath))
            expected_title = "Automation Exercise - All Products"
            actual_title = self.page_title()  # Retrieve using driver.title
            assert actual_title == expected_title, "Title does not match"
        except Exception as e:
            print(f"Page not found : {e}")

    def validateAllProducts(self):
        try:
            #assert self.validateElement(*self.div_allProducts_xpath),"All Products section not found"
            assert self.validateMsg(self.div_allProducts_xpath), "All Products section not found"
        except Exception as e:
                print("The error is: ", e)

    def searchProduct(self):
        try:
          self.inputText("Top",self.txt_search_id)
          self.clickElement(self.btn_searchSubmit_id)
        except Exception as e:
                print("The error is: ", e)

    def validateSearchedProd(self):
        assert self.validateMsg(self.txt_searchedProd_xpath),"Searched Products section not found"


        # Locators
        # This selects the 'Price' tag inside every product block
    ALL_PRICES = (By.XPATH, "//div[@class='productinfo text-center']/h2")
    CONTINUE_SHOPPING = (By.XPATH, "//button[text()='Continue Shopping']")

    # def add_products_above_price(self, threshold):
    #     """
    #     Finds products, filters by price, and adds them to cart
    #     by bypassing Ad overlays (like aswift_2) using JavaScript.
    #     """
    #     # 1. Senior Move: Clear any existing ads before starting
    #     self.remove_ads_from_dom()
    #
    #     # 2. Get the initial list of price elements
    #     price_elements = self.getElements(self.ALL_PRICES)
    #
    #     for i in range(len(price_elements)):
    #         try:
    #             # Re-fetch elements in each iteration to prevent StaleElementReferenceException
    #             # This is necessary because the site's ad-refreshes often reload the DOM
    #             current_prices = self.getElements(self.ALL_PRICES)
    #             price_element = current_prices[i]
    #
    #             # Clean the price text: "Rs. 1,500" -> 1500
    #             price_text = price_element.text
    #             clean_price = price_text.replace("Rs. ", "").replace(",", "").strip()
    #
    #             if not clean_price:
    #                 continue
    #
    #             numeric_price = int(clean_price)
    #
    #             if numeric_price > threshold:
    #                 # 3. Scroll the element to the CENTER of the screen
    #                 # Standard scroll puts it at the top, where sticky headers/ads hide it
    #                 self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", price_element)
    #                 time.sleep(1)
    #
    #                 # 4. Find the 'Add to Cart' button relative to the price
    #                 add_to_cart_btn = price_element.find_element(By.XPATH, "./following-sibling::a")
    #
    #                 # 5. THE FIX: JavaScript Click
    #                 # This ignores the 'aswift_2' iframe entirely and triggers the click on the button
    #                 self.driver.execute_script("arguments[0].click();", add_to_cart_btn)
    #                 print(f"Added product with price: {numeric_price}")
    #
    #                 # 6. Wait for 'Continue Shopping' modal and click it
    #                 # We use a standard wait here to ensure the action was successful
    #                 self.wait.until(EC.element_to_be_clickable(self.CONTINUE_SHOPPING)).click()
    #
    #                 # Small delay to let the modal overlay vanish before the next scroll
    #                 time.sleep(0.5)
    #
    #         except (StaleElementReferenceException, Exception) as e:
    #             # If an element goes stale or a price is missing, skip to the next
    #             print(f"Skipping index {i} due to: {e}")
    #             continue

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

