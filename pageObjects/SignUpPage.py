from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.BasePage import BasePage


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
        #self.wait = WebDriverWait(self.driver, 5)

    def validatePageTitle(self):
        try:
            #self.waitForElement((By.XPATH,self.txt_Account_xpath))
            expected_title = "Automation Exercise - Signup"
            actual_title = self.page_title()  # Retrieve using driver.title
            assert actual_title == expected_title, "Title does not match"
        except Exception as e:
            print(f"Page not found : {e}")


    def validateInfo(self):
        try:
            return self.driver.find_element(*self.txt_info_xpath).is_displayed()
        except Exception as e:
            print("The error is: ", e)

    def clickOnMr(self):
        try:
            self.driver.find_element(*self.rdo_mr_xpath).click()
        except Exception as e:
            print("The error is: ", e)

    def clickOnMrs(self):
        try:
            self.driver.find_element(*self.rdo_mrs_xpath).click()
        except Exception as e:
            print("The error is: ", e)

    # def setUsername(self,random_name):
    #     try:
    #         self.driver.find_element(self.txt_name_id).send_keys(random_name)
    #     except Exception as e:
    #         print("The error is: ", e)
    #
    # def setEmailID(self,random_email):
    #     try:
    #         self.driver.find_element(self.txt_email_id).send_keys(random_email)
    #     except Exception as e:
    #         print("The error is: ", e)

    def setPassword(self,pwd):
        try:
            self.driver.find_element(*self.txt_pwd_id).send_keys(pwd)
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
            dropmonth=self.driver.find_element(*self.dd_month_xpath)
            select=Select(dropmonth)
            select.select_by_value(month)
        except Exception as e:
            print("The error is: ", e)

    def selectYears(self, year):
        try:
            dropyear=self.driver.find_element(*self.dd_year_xpath)
            select=Select(dropyear)
            select.select_by_value(year)
        except Exception as e:
            print("The error is: ", e)

    def clickNewsCbk(self):
        try:
            self.driver.find_element(*self.cbx_news_id).click()
        except Exception as e:
            print("The error is: ", e)

    def clickOffer(self):
        try:
            self.driver.find_element(*self.cbx_offer_id).click()
        except Exception as e:
            print("The error is: ", e)

    def setFirstName(self,fname):
        try:
            self.driver.find_element(*self.txt_fname_id).send_keys(fname)
        except Exception as e:
            print("The error is: ", e)

    def setLastName(self,lname):
        try:
            self.driver.find_element(*self.txt_lname_id).send_keys(lname)
        except Exception as e:
            print("The error is: ", e)

    def setCompanyName(self,cname):
        try:
            self.driver.find_element(*self.txt_company_id).send_keys(cname)
        except Exception as e:
            print("The error is: ", e)

    def setAddress1(self,address1):
        try:
            self.driver.find_element(*self.txt_address1_id).send_keys(address1)
        except Exception as e:
            print("The error is: ", e)

    def setAddress2(self,address2):
        try:
            self.driver.find_element(*self.txt_address2_id).send_keys(address2)
        except Exception as e:
            print("The error is: ", e)

    def selectCountry(self,country):
        try:
            dropCountry=self.driver.find_element(*self.dd_country_xpath)
            select=Select(dropCountry)
            select.select_by_value(country)
        except Exception as e:
            print("The error is: ", e)

    def setState(self,state):
        try:
            self.driver.find_element(*self.txt_state_id).send_keys(state)
        except Exception as e:
            print("The error is: ", e)

    def setCity(self,city):
        try:
            self.driver.find_element(*self.txt_city_id).send_keys(city)
        except Exception as e:
            print("The error is: ", e)

    def setZipCode(self,zipcode):
        try:
            self.driver.find_element(*self.txt_zip_id).send_keys(zipcode)
        except Exception as e:
            print("The error is: ", e)

    def setMobileNumber(self,mobile):
        try:
            self.driver.find_element(*self.txt_mobile_id).send_keys(mobile)
        except Exception as e:
            print("The error is: ", e)

    def clickCreateAcc(self):
        try:
            self.scroll_to_and_click(self.btn_create_Acc_xpath)
        except Exception as e:
            print("The error is that: ", e)

