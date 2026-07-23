# from selenium.webdriver.common.by import By
# from constants.ui_constants import Titles, Messages
# from pages.BasePage import BasePage
#
#
# class AccountRegistrationPage(BasePage):
#     txt_user_xpath=(By.XPATH,"//input[@placeholder='Name']")
#     txt_email_xpath=(By.XPATH,"//input[@data-qa='signup-email']")
#     lnk_signup_xpath=(By.XPATH,"//button[normalize-space()='Signup']")
#     lnk_ad_xpath=(By.XPATH,"//div[@class='grippy-host']")
#     txt_loginEmail_xpath = (By.XPATH, "//input[@data-qa='login-email']")
#     txt_password_name = (By.NAME, "password")
#     btn_login_xpath = (By.XPATH, "//button[@data-qa='login-button']")
#     txt_errorMsg_xpath = (By.XPATH,"//p[text()='Your email or password is incorrect!']")
#
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#
#     def validatePageTitle(self):
#         actual_title = self.driver.title
#         assert actual_title == Titles.REGISTER,f"Expected Registration Page Title is: {Titles.REGISTER} and the Actual Registration Page Title is: {actual_title}"
#
#     def clickOnAd(self):
#         self.driver.find_element(*self.lnk_ad_xpath).click()
#
#     def setName(self,name):
#         self.driver.find_element(*self.txt_user_xpath).send_keys(name)
#
#     # def setEmail(self,pwd):
#     #     self.driver.find_element(self.lnk_email_xpath).send_keys(pwd)
#
#     def setEmail(self,random_email):
#         try:
#             self.driver.find_element(*self.txt_email_xpath).send_keys(random_email)
#         except Exception as e:
#             print("The error is: ", e)
#
#     def clickSignup(self):
#         self.driver.find_element(*self.lnk_signup_xpath).click()
#
#     def setUserEmail(self, random_email):
#         try:
#             self.driver.find_element(*self.txt_loginEmail_xpath).send_keys(random_email)
#         except Exception as e:
#             print("The error is: ", e)
#
#     def setPassword(self, pwd):
#         try:
#             self.driver.find_element(*self.txt_password_name).send_keys(pwd)
#         except Exception as e:
#             print("The error is: ", e)
#
#     def clickLogin(self):
#         self.driver.find_element(*self.btn_login_xpath).click()
#
#     def login(self, existing_user, reg_password):
#
#         self.setUserEmail(existing_user)
#
#         self.setPassword(reg_password)
#
#         self.clickLogin()
#
#         return self

from selenium.webdriver.common.by import By
from constants.ui_constants import Titles
from pages.BasePage import BasePage


class AccountRegistrationPage(BasePage):
    txt_user_xpath=(By.XPATH,"//input[@placeholder='Name']")
    txt_email_xpath=(By.XPATH,"//input[@data-qa='signup-email']")
    lnk_signup_xpath=(By.XPATH,"//button[normalize-space()='Signup']")
    lnk_ad_xpath=(By.XPATH,"//div[@class='grippy-host']")
    txt_loginEmail_xpath = (By.XPATH, "//input[@data-qa='login-email']")
    txt_password_name = (By.NAME, "password")
    btn_login_xpath = (By.XPATH, "//button[@data-qa='login-button']")
    txt_errorMsg_xpath = (By.XPATH,"//p[text()='Your email or password is incorrect!']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def validatePageTitle(self):
        actual_title = self.driver.title
        assert actual_title == Titles.REGISTER,f"Expected Registration Page Title is: {Titles.REGISTER} and the Actual Registration Page Title is: {actual_title}"

    def clickOnAd(self):
        self.find(*self.lnk_ad_xpath).click()

    def setName(self,name):
        self.find(*self.txt_user_xpath).send_keys(name)

    # def setEmail(self,pwd):
    #     self.driver.find_element(self.lnk_email_xpath).send_keys(pwd)

    def setEmail(self,random_email):
        try:
            self.find(*self.txt_email_xpath).send_keys(random_email)
        except Exception as e:
            print("The error is: ", e)

    def clickSignup(self):
        self.find(*self.lnk_signup_xpath).click()

    def setUserEmail(self, random_email):
        try:
            self.find(*self.txt_loginEmail_xpath).send_keys(random_email)
        except Exception as e:
            print("The error is: ", e)

    def setPassword(self, pwd):
        try:
            self.find(*self.txt_password_name).send_keys(pwd)
        except Exception as e:
            print("The error is: ", e)

    def clickLogin(self):
        self.find(*self.btn_login_xpath).click()

    def login(self, existing_user, reg_password):

        self.setUserEmail(existing_user)

        self.setPassword(reg_password)

        self.clickLogin()

        return self





