
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from constants.ui_constants import Titles
from core.config import get_base_url

class HomePage(BasePage):
    lnk_login_xpath=(By.XPATH,"//a[normalize-space()='Signup / Login']")
    lnk_delAcc_xpath = (By.XPATH,"//a[text()=' Delete Account']")
    lnk_logout_xpath = (By.XPATH,"//a[text()=' Logout']")
    txt_loggedIn_xpath = (By.XPATH,"//a[text()=' Logged in as ']")
    txt_featuresItems_xpath = (By.XPATH,"//div[@class='features_items']")
    txt_recomItems_xpath =(By.XPATH,"//div[@class='recommended_items']")
    txt_catProds_xpath = (By.XPATH,"//div[@id='accordian']")
    txt_brands_xpath = (By.XPATH,"//div[@class='brands_products']")
    lnk_products_xpath = (By.XPATH, "//a[text()=' Products']") #"//a[text()=' Products']"
    lnk_deleteAccount_xpath = (By.XPATH, "//a[@href='/delete_account']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def openURL(self):
        self.driver.get(get_base_url())

    def validatePageTitle(self):
        try:
            #self.waitForElement((By.XPATH,self.txt_Account_xpath))
            expected_title = "Automation Exercise"
            actual_title = self.page_title()  # Retrieve using driver.title
            assert actual_title == expected_title, "Title does not match"
        except Exception as e:
            print(f"Page not found : {e}")
    def validatePageTitle1(self):
        actual_title = self.driver.title
        assert actual_title == Titles.HOME, f"Expected Home Page Title is: {Titles.HOME} and the Actual Home Page Title is: {actual_title}"


    def clickLogin(self):
        self.find(*self.lnk_login_xpath).click()

    def validate_deleteAccount(self):
        try:
            return self.find(*self.lnk_delAcc_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validate_logout(self):
        try:
            return self.find(*self.lnk_logout_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    # def validate_loggedIn(self):
    #     try:
    #         self.driver.wait_for_element(*self.txt_loggedIn_xpath)
    #         return self.driver.find_element(*self.txt_loggedIn_xpath).is_displayed()
    #     except Exception as e:
    #         print(f"Element not found : {e}")

    def validate_loggedIn(self):
        try:
            return self.find(*self.txt_loggedIn_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")
            return False

    def validate_featuresItems(self):
        try:
            return self.find(*self.txt_featuresItems_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateCategoryItems(self):
        try:
            return self.find(*self.txt_catProds_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateBrands(self):
        try:
            return self.find(*self.txt_brands_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateRecommendedItems(self):
        try:
            return self.find(*self.txt_recomItems_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateProductsLnk(self):
        try:
            return self.find(*self.lnk_products_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def clickProducts(self):
        try:
            self.clickElement(self.lnk_products_xpath)
            #self.handle_google_vignette()  # AD popup close
        except Exception as e:
            print("The error is that: ", e)

    def clickLogout(self):
        try:
            self.scroll_to_and_click(self.lnk_logout_xpath)
        except Exception as e:
            print("The error is that: ", e)

    def validateUserName(self, expected_name):
        # Use .text instead of get_attribute("value")
        # Ensure self.txt_loggedIn_xpath is a string (e.g., "//a[contains(text(), 'Logged in as')]")
        element = self.find(*self.txt_loggedIn_xpath)

        full_status_text = element.text
        #print(full_status_text)

        actual_name = full_status_text.split("as ")[-1].strip()

       # Assertion
        assert actual_name == expected_name, f"Expected user {expected_name} but found {actual_name}"

    def deleteAccount(self):
        self.scroll_to_and_click(self.lnk_deleteAccount_xpath)
