import os
import time

from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class OrderPlacedPage(BasePage):
    txt_orderPlaced_xpath = (By.XPATH,"//b[text()='Order Placed!']")
    txt_orderConfirm_xpath = (By.XPATH,"//p[text()='Congratulations! Your order has been confirmed!']")
    btn_dnloadInvoice_xpath =(By.XPATH,"//a[text()='Download Invoice']")
    btn_continue_xpath = (By.XPATH,"//a[text()='Continue']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    def validateOrderPlaced(self):
        try:
            return self.driver.find_element(*self.txt_orderPlaced_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validatePageTitle(self):
        try:
            #self.waitForElement((By.XPATH,self.txt_Account_xpath))
            expected_title = "Automation Exercise - Order Placed"
            actual_title = self.page_title()  # Retrieve using driver.title
            assert actual_title == expected_title, "Title does not match"
        except Exception as e:
            print(f"Page not found : {e}")

    def validateOrderConfirmMsg(self):
        try:
            return self.driver.find_element(*self.txt_orderConfirm_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    # def clickNewsCbk(self):
    #     try:
    #         self.driver.find_element(*self.cbx_news_id).click()
    #     except Exception as e:
    #         print("The error is: ", e)

    def downloadInvoice(self):
        #self.clickElement(self.btn_dnloadInvoice_xpath)
        self.click_element(self.btn_dnloadInvoice_xpath)
        # Give the file a few seconds to actually hit the hard drive
        time.sleep(3)

    def verifyInvoiceDownloaded(self, file_name):
        """
        Checks if the file exists in the project's 'downloads' folder.
        """
        path = os.path.join(os.getcwd(), "downloads", file_name)
        return os.path.exists(path)


    def clickContinue(self):
        try:
            #self.clickElement(self.btn_continue_xpath)
            #self.click_element(self.btn_continue_xpath)
            self.click_and_bypass(self.btn_continue_xpath, "automationexercise.com")
        except Exception as e:
            print(f"Element not found : {e}")



