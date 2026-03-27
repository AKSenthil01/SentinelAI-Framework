from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class CheckoutPage(BasePage):
    btn_placeOrder_xpath = (By.XPATH,"//a[text()='Place Order']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickOnPlaceOrder(self):
           try:
               #self.clickElement(self.btn_placeOrder_xpath)
               self.scroll_to_and_click(self.btn_placeOrder_xpath)
           except Exception as e:
               print(f"Place Order option does not exists: {e}")


