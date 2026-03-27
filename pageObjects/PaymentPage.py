from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


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
        try:
            #self.waitForElement((By.XPATH,self.txt_Account_xpath))
            expected_title = "Automation Exercise - Payment"
            actual_title = self.page_title()  # Retrieve using driver.title
            assert actual_title == expected_title, "Title does not match"
        except Exception as e:
            print(f"Page not found : {e}")

    # def pay_with_card(self,name,number,cvc,month,year):
    #     self.inputText(self.txt_name_on_card, name)
    #     self.inputText(self.txt_card_number, number)
    #     self.inputText(self.txt_cvc_number, cvc)
    #     self.inputText(self.txt_expiry_month, month)
    #     self.inputText(self.txt_expiry_year, year)
    #     self.clickElement(self.txt_pay_confirmed)
    def pay_with_card(self,name,number,cvc,month,year):
        self.inputText(name,self.txt_name_on_card)
        self.inputText(number,self.txt_card_number)
        self.inputText(cvc , self.txt_cvc_number)
        self.inputText(month,self.txt_expiry_month )
        self.inputText(year,self.txt_expiry_year)
        #self.clickElement(self.txt_pay_confirmed)
        self.scroll_to_and_click(self.txt_pay_confirmed)

