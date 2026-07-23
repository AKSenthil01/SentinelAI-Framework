from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from constants.ui_constants import Titles



class PaymentPage(BasePage):
    txt_name_on_card = (By.NAME, "name_on_card")
    txt_card_number = (By.NAME, "card_number")
    txt_cvc_number = (By.NAME, "cvc")
    txt_expiry_month = (By.NAME, "expiry_month")
    txt_expiry_year = (By.NAME, "expiry_year")
    txt_pay_confirmed = (By.ID, "submit")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def validatePageTitle(self):
        actual_title = self.driver.title
        assert actual_title == Titles.PAYMENT, f"Expected Payment Page Title is: {Titles.PAYMENT} and the Actual Payment Page Title is: {actual_title}"

    def pay_with_card(self,name,number,cvc,month,year):
        self.inputText(self.txt_name_on_card,name)
        self.inputText(self.txt_card_number,number)
        self.inputText(self.txt_cvc_number,cvc)
        self.inputText(self.txt_expiry_month ,month)
        self.inputText(self.txt_expiry_year,year)
        self.scroll_to_and_click(self.txt_pay_confirmed)
        # WebDriverUtils.safe_click(
        #      self.driver,
        #      self.txt_pay_confirmed
        #  )
        return self

