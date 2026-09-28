from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.click_helper import ClickHelper
from pages.BasePage import BasePage
from constants.ui_constants import Titles
from utils.self_healing import SelfHealing


class PaymentPageAIDemo(BasePage):

    txt_name_on_card = (By.NAME, "name_on_card")
    txt_card_number = (By.NAME, "card_number")
    txt_cvc_number = (By.NAME, "cvc")
    txt_expiry_month = (By.NAME, "expiry_month")
    txt_expiry_year = (By.NAME, "expiry_year")

    #
    # Purposely wrong locator
    #
    txt_pay_confirmed = (
        By.ID,
        "confirm_payment_button_ai_demo"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def validatePageTitle(self):
        actual = self.driver.title

        assert actual == Titles.PAYMENT

    def pay_with_card(
            self,
            name,
            number,
            cvc,
            month,
            year
    ):

        self.inputText(self.txt_name_on_card, name)
        self.inputText(self.txt_card_number, number)
        self.inputText(self.txt_cvc_number, cvc)
        self.inputText(self.txt_expiry_month, month)
        self.inputText(self.txt_expiry_year, year)

        #
        # AI healing happens here
        #

        pay_button = SelfHealing.find(
            self.driver,
            self.wait,
            self.txt_pay_confirmed,
            EC.element_to_be_clickable
        )

        ClickHelper.click(
            self.driver,
            pay_button
        )

        #
        # Wait until Order Placed page opens
        #

        self.wait.until(

            EC.visibility_of_element_located(

                (
                    By.XPATH,
                    "//b[text()='Order Placed!']"
                )

            )

        )

        print("Payment successful")

        return self

