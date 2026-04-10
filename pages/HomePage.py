import pytest
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from constants.ui_constants import Titles, Messages

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
        self.driver.find_element(*self.lnk_login_xpath).click()

    def validate_deleteAccount(self):
        try:
            return self.driver.find_element(*self.lnk_delAcc_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validate_logout(self):
        try:
            return self.driver.find_element(*self.lnk_logout_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validate_loggedIn(self):
        try:
            self.driver.wait_for_element(*self.txt_loggedIn_xpath)
            return self.driver.find_element(*self.txt_loggedIn_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validate_featuresItems(self):
        try:
            return self.driver.find_element(*self.txt_featuresItems_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateCategoryItems(self):
        try:
            return self.driver.find_element(*self.txt_catProds_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateBrands(self):
        try:
            return self.driver.find_element(*self.txt_brands_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateRecommendedItems(self):
        try:
            return self.driver.find_element(*self.txt_recomItems_xpath).is_displayed()
        except Exception as e:
            print(f"Element not found : {e}")

    def validateProductsLnk(self):
        try:
            return self.driver.find_element(*self.lnk_products_xpath).is_displayed()
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

    # def validateUserName(self,username):
    #     full_status_text=(self.driver.find_element(By.XPATH,self.txt_loggedIn_xpath)).get_attribute("value")
    #     #full_status_text = element.text
    #     print(f"Full text found: {full_status_text}")
    #
    #         # Extract the username
    #         # Splitting by "as " and taking the part that comes after it
    #     if "as " in full_status_text:
    #         extracted_username = full_status_text.split("as ")[-1].strip()
    #     else:
    #         pytest.fail(f"Unexpected status text format: {full_status_text}")
    #         # Assertions
    #     assert extracted_username == self.username, f"Expected 'username' but got '{extracted_username}'"
    #     print(f"Successfully validated user: {extracted_username}")
    #
    #
    #
    def validateUserName(self, expected_name):
        # Use .text instead of get_attribute("value")
        # Ensure self.txt_loggedIn_xpath is a string (e.g., "//a[contains(text(), 'Logged in as')]")
        element = self.driver.find_element(*self.txt_loggedIn_xpath)

        full_status_text = element.text
        #print(full_status_text)

        #self.logger.info(f"Captured status text: {full_status_text}")

        # Extract the name using the split logic we discussed
        # if "as " in full_status_text:
        #     # Splits "Logged in as username" -> ["Logged in ", "username"]
        #     actual_name = full_status_text.split("as ")[-1].strip()
        # else:
        #     actual_name = full_status_text  # Fallback
        actual_name = full_status_text.split("as ")[-1].strip()

        #print(actual_name)
        # Assertion
        assert actual_name == expected_name, f"Expected user {expected_name} but found {actual_name}"

    def deleteAccount(self):
        self.scroll_to_and_click(self.lnk_deleteAccount_xpath)
        #self.driver.find_element(*self.lnk_deleteAccount_xpath).click()