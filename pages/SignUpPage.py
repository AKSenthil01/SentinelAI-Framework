from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from constants.ui_constants import Titles, Messages

class SignUp(BasePage):
    txt_info_xpath=(By.XPATH,"//b[normalize-space()='Enter Account Information']")
    rdo_mr_xpath=(By.XPATH,"//input[@value='Mr']")
    rdo_mrs_xpath = (By.XPATH,"//input[@value='Mrs']")
    txt_name_id =(By.ID, "name")
    txt_email_id = (By.ID,"email")
    txt_pwd_id = (By.ID,"password")
    dd_day_xpath = (By.XPATH,"//select[@id='days']")
    dd_month_xpath = (By.XPATH,"//select[@id='months']")
    dd_year_xpath = (By.XPATH,"//select[@id='years']")
    cbx_news_id = (By.ID,"newsletter")
    cbx_offer_id = (By.ID,"optin")
    txt_fname_id = (By.ID,"first_name")
    txt_lname_id = (By.ID,"last_name")
    txt_company_id = (By.ID,"company")
    txt_address1_id = (By.ID,"address1")
    txt_address2_id = (By.ID,"address2")
    dd_country_xpath = (By.XPATH,"//select[@id='country']")
    txt_state_id = (By.ID,"state")
    txt_city_id = (By.ID,"city")
    txt_zip_id = (By.ID,"zipcode")
    txt_mobile_id = (By.ID,"mobile_number")
    btn_create_Acc_xpath = (By.XPATH,"//button[text()='Create Account']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    def validatePageTitle(self):
        actual_title = self.driver.title
        assert actual_title == Titles.SIGNUP, f"Expected Signup Page Title is: {Titles.SIGNUP} and the Actual Signup Page Title is: {actual_title}"

    def validateInfo(self):
        try:
            return self.find(*self.txt_info_xpath).is_displayed()
        except Exception as e:
            print("The error is: ", e)

    def clickOnMr(self):
        try:
            self.find(*self.rdo_mr_xpath).click()
        except Exception as e:
            print("The error is: ", e)

    def clickOnMrs(self):
        try:
            self.find(*self.rdo_mrs_xpath).click()
        except Exception as e:
            print("The error is: ", e)

    def setPassword(self,pwd):
        try:
            self.find(*self.txt_pwd_id).send_keys(pwd)
        except Exception as e:
            print("The error is: ", e)

    def selectDays(self, day):
        try:
            dropDay=self.driver.find_element(*self.dd_day_xpath)
            select=Select(dropDay)
            select.select_by_value(day)
        except Exception as e:
            print("The error is: ", e)

    def selectMonths(self, month):
        try:
            dropmonth=self.find(*self.dd_month_xpath)
            select=Select(dropmonth)
            select.select_by_value(month)
        except Exception as e:
            print("The error is: ", e)

    def selectYears(self, year):
        try:
            dropyear=self.find(*self.dd_year_xpath)
            select=Select(dropyear)
            select.select_by_value(year)
        except Exception as e:
            print("The error is: ", e)

    def clickNewsCbk(self):
        try:
            self.find(*self.cbx_news_id).click()
        except Exception as e:
            print("The error is: ", e)

    def clickOffer(self):
        try:
            self.find(*self.cbx_offer_id).click()
        except Exception as e:
            print("The error is: ", e)

    def setFirstName(self,fname):
        try:
            self.find(*self.txt_fname_id).send_keys(fname)
        except Exception as e:
            print("The error is: ", e)

    def setLastName(self,lname):
        try:
            self.find(*self.txt_lname_id).send_keys(lname)
        except Exception as e:
            print("The error is: ", e)

    def setCompanyName(self,cname):
        try:
            self.find(*self.txt_company_id).send_keys(cname)
        except Exception as e:
            print("The error is: ", e)

    def setAddress1(self,address1):
        try:
            self.find(*self.txt_address1_id).send_keys(address1)
        except Exception as e:
            print("The error is: ", e)

    def setAddress2(self,address2):
        try:
            self.find(*self.txt_address2_id).send_keys(address2)
        except Exception as e:
            print("The error is: ", e)

    def selectCountry(self,country):
        try:
            dropCountry=self.find(*self.dd_country_xpath)
            select=Select(dropCountry)
            select.select_by_value(country)
        except Exception as e:
            print("The error is: ", e)

    def setState(self,state):
        try:
            self.find(*self.txt_state_id).send_keys(state)
        except Exception as e:
            print("The error is: ", e)

    def setCity(self,city):
        try:
            self.find(*self.txt_city_id).send_keys(city)
        except Exception as e:
            print("The error is: ", e)

    def setZipCode(self,zipcode):
        try:
            self.find(*self.txt_zip_id).send_keys(zipcode)
        except Exception as e:
            print("The error is: ", e)

    def setMobileNumber(self,mobile):
        try:
            self.find(*self.txt_mobile_id).send_keys(mobile)
        except Exception as e:
            print("The error is: ", e)

    def clickCreateAcc(self):
        try:
            self.scroll_to_and_click(self.btn_create_Acc_xpath)
        except Exception as e:
            print("The error is that: ", e)

