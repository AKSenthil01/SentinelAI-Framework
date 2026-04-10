import time


from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage
from constants.ui_constants import Titles, Messages


class AccountCreatedPage(BasePage):
    txt_Account_xpath=(By.XPATH,"//h2[@data-qa='account-created']")
    txt_msg1_xpath=(By.XPATH, "//p[text()='Congratulations! Your new account has been successfully created!']")
    txt_msg2_xpath=(By.XPATH, "//p[text()='You can now take advantage of member privileges to enhance your online shopping experience with us.']")
    btn_continue_xpath=(By.XPATH,"//a[text()='Continue']")
    btn_skipAd_Id=(By.ID, "//div[@id='dismiss-button']")
    txt_accountDeleted_xpath=(By.XPATH, "//h2[@data-qa='account-deleted']")
    txt_deletedMsg1_xpath = (By.XPATH, "//p[text()='Your account has been permanently deleted!']")
    txt_deletedMsg2_xpath = (By.XPATH, "//p[text()='You can create new account to take advantage of member privileges to enhance your online shopping experience with us.']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = WebDriverWait(self.driver, 5)

    def validateAccountCreation(self):
        try:
            return self.driver.find_element(*self.txt_Account_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateSuccessMsg1(self):
        try:
            return self.driver.find_element(*self.txt_msg1_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateSuccessMsg2(self):
        try:
            return self.driver.find_element(*self.txt_msg2_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def clickContinueBtn(self):
        try:
            #self.driver.find_element(*self.btn_continue_xpath).click()
            #self.scroll_to_and_click(self.btn_continue_xpath)
            #self.click_button_safely(self.btn_continue_xpath)
            #self.click_element(self.btn_continue_xpath)  # Ads are handled automatically!
            #self.click_and_bypass_fast(self.btn_continue_xpath)  # Ads are handled automatically!
            self.click_and_bypass(self.btn_continue_xpath, "automationexercise.com")

        except Exception as e:
            print(f"Element not found : {e}")

    def click_continue_and_skip_ad(self):
        """
        If clicking triggers an ad, we manually force the browser
        to the 'clean' destination.
        """
        self.driver.find_element(*self.btn_continue_xpath).click()

        # Give the browser a split second to check the URL
        import time
        time.sleep(1)

        if "#google_vignette" in self.driver.current_url:
            print("Ad detected even with UC. Forcing navigation...")
            # Strip everything after the # to get the real page
            real_url = self.driver.current_url.split("#")[0]
            self.driver.get(real_url)

    # def validatePageTitle(self):
    #     try:
    #         #self.waitForElement((By.XPATH,self.txt_Account_xpath))
    #         expected_title = "Automation Exercise - Account Created"
    #         actual_title = self.page_title()  # Retrieve using driver.title
    #         assert actual_title == expected_title, "Title does not match"
    #     except Exception as e:
    #         print(f"Page not found : {e}")

    def validatePageTitle(self):
        actual_title = self.driver.title
        assert actual_title == Titles.ACCOUNT, f"Expected Home Page Title is: {Titles.ACCOUNT} and the Actual Home Page Title is: {actual_title}"


    def handleAdPopup(self):
        #close_btn = (By.XPATH, "//button[text()='Close'] | //u[text()='Continue Shopping']")
        try:
            # Check for 3 seconds if the popup appears
            #self.scroll_to_and_click(self.btn_skipAd_Id).click()
            element = self.wait.until(EC.element_to_be_clickable(self.btn_skipAd_Id))
            element.click()
        except TimeoutException:
            # If no popup appears, just move on
            pass


    def validateAccountDelete(self):
        try:
            return self.driver.find_element(*self.txt_accountDeleted_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateDeleteMsg1(self):
        try:
            return self.driver.find_element(*self.txt_deletedMsg1_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateDeleteMsg2(self):
        try:
            return self.driver.find_element(*self.txt_deletedMsg2_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")
