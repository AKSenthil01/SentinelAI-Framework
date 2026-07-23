import os
import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from constants.ui_constants import Titles

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
            return self.find(*self.txt_orderPlaced_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validatePageTitle(self):
        actual_title = self.driver.title
        assert actual_title == Titles.ORDER, f"Expected Orders Page Title is: {Titles.ORDER} and the Actual Orders Page Title is: {actual_title}"


    def validateOrderConfirmMsg(self):
        try:
            return self.find(*self.txt_orderConfirm_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def downloadInvoice(self):
        self.clickElement(self.btn_dnloadInvoice_xpath)
        #self.click_element(self.btn_dnloadInvoice_xpath)
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
            #self.click_and_bypass(self.btn_continue_xpath, "automationexercise.com")
            self.click_and_bypass(self.btn_continue_xpath)
        except Exception as e:
            print(f"Element not found : {e}")

    def verify_order_success(self):

        assert self.validateOrderPlaced(), \
            "Order Placed message not displayed."

        assert self.validateOrderConfirmMsg(), \
            "Order Confirmation message not displayed."

        return self

    def download_invoice(self, file_name):

        self.downloadInvoice()

        assert self.verifyInvoiceDownloaded(file_name), \
            f"Invoice '{file_name}' was not downloaded."

        return self

    def continue_shopping(self):

        self.clickContinue()

        return self



