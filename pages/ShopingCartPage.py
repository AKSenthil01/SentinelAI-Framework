from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from constants.ui_constants import Titles

class ShopingCartPage(BasePage):

    btn_proceedToCheckout_xpath = (By.XPATH,"//a[text()='Proceed To Checkout']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def validatePageTitle(self):
        actual_title = self.driver.title
        assert actual_title == Titles.CART, f"Expected Cart Page Title is: {Titles.CART} and the Actual Cart Page Title is: {actual_title}"

    def clickProceedToCheckout(self):
        try:
            self.scroll_to_and_click(self.btn_proceedToCheckout_xpath)
        except Exception as e:
            print(f"Proceed to Checkout option does not exists : {e}")


