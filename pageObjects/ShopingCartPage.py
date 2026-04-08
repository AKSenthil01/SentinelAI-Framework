from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class ShopingCartPage(BasePage):

    btn_proceedToCheckout_xpath = (By.XPATH,"//a[text()='Proceed To Checkout']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def validatePageTitle(self):
        try:
            #self.waitForElement((By.XPATH,self.txt_Account_xpath))
            expected_title = "Automation Exercise - Checkout"
            actual_title = self.page_title()  # Retrieve using driver.title
            assert actual_title == expected_title, "Title does not match"
        except Exception as e:
            print(f"Page not found : {e}")


    def clickProceedToCheckout(self):
        try:
            #self.clickElement(self.btn_proceedToCheckout_xpath)
            self.scroll_to_and_click(self.btn_proceedToCheckout_xpath)
        except Exception as e:
            print(f"Proceed to Checkout option does not exists : {e}")


