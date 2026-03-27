from selenium.webdriver.common.by import By
class AccountRegistrationPage:
    txt_user_xpath=(By.XPATH,"//input[@placeholder='Name']")
    txt_email_xpath=(By.XPATH,"//input[@data-qa='signup-email']")
    lnk_signup_xpath=(By.XPATH,"//button[normalize-space()='Signup']")
    lnk_ad_xpath=(By.XPATH,"//div[@class='grippy-host']")

    def __init__(self,driver):
        self.driver = driver

    def validatePageTitle(self):
        try:
            #self.waitForElement((By.XPATH,self.txt_Account_xpath))
            expected_title = "Automation Exercise - Signup / Login"
            actual_title = self.page_title()  # Retrieve using driver.title
            assert actual_title == expected_title, "Title does not match"
        except Exception as e:
            print(f"Page not found : {e}")

    def clickOnAd(self):
        self.driver.find_element(*self.lnk_ad_xpath).click()

    def setName(self,name):
        self.driver.find_element(*self.txt_user_xpath).send_keys(name)

    # def setEmail(self,pwd):
    #     self.driver.find_element(self.lnk_email_xpath).send_keys(pwd)

    def setEmail(self,random_email):
        try:
            self.driver.find_element(*self.txt_email_xpath).send_keys(random_email)
        except Exception as e:
            print("The error is: ", e)

    def clickSignup(self):
        self.driver.find_element(*self.lnk_signup_xpath).click()







