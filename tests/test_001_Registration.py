import logging
#import time

from pages.AccountCreatedPage import AccountCreatedPage


from pages.AccountRegistrationPage import AccountRegistrationPage
from pages.AllProductsPage import AllProductsPage
from pages.CheckOutPage import CheckoutPage
from pages.HomePage import HomePage
from pages.OrderPlacedPage import OrderPlacedPage
from pages.PaymentPage import PaymentPage
from pages.ShopingCartPage import ShopingCartPage

from pages.SignUpPage import SignUp
from utils.customLogger import get_custom_logger
from core.config import get_base_url
from utils.data_loader import load_test_data


class Test001Register:
    logger = get_custom_logger(__name__)
    data = load_test_data()

    def test_Register(self, setup, random_name, random_email ,reg_password):
        self.logger.info("*****test_001_AccountRegistration started*****")
        self.driver=setup
        self.driver.get(get_base_url())
        self.logger.info("*****Launching Application*****")
        self.driver.maximize_window()
        #self.driver.implicitly_wait(10)
        self.HP=HomePage(self.driver)
        self.HP.validatePageTitle()
        self.logger.info("*****Validating Home Page Title*****")
        self.HP.clickLogin()
        self.logger.info("*****Clicking on Login link*****")
        #self.driver.implicitly_wait(10)
        self.AccReg=AccountRegistrationPage(self.driver)
        #self.driver.implicitly_wait(10)
        self.AccReg.validatePageTitle()
        self.logger.info("*****Validating Account Registration Page Title*****")
        #self.AccReg.clickOnAd()
        self.logger.info("*****Entering user name and password on Registration page*****")
        self.AccReg.setName(random_name)
        self.AccReg.setEmail(random_email)
        self.AccReg.clickSignup()
        self.logger.info("*****Clicking on Signup link*****")
        self.driver.implicitly_wait(10)
        self.SP=SignUp(self.driver)
        self.SP.validatePageTitle()
        self.logger.info("*****Validating SignUp Page Title*****")
        self.msg=self.SP.validateInfo()
        #print(self.msg)
        self.logger.info("*****Validating the message*****")
        if self.msg:
            self.logger.info("*******Message validation successful...*****")
            assert True
        else:
            self.logger.info("*******Message validation failed...*****")
            assert False ,"The displayed message is not as expected"
        #self.logger.info("*****test_001_AccountRegistration completed*****")
        self.SP.clickOnMr()
        self.logger.info("*****Clicking on Mr. radiobutton*****")
        #self.SP.setPassword("Senpass77")
        self.SP.setPassword(reg_password)
        self.logger.info("*****Setting Password*******")
        self.SP.selectDays(self.data["customer"]["days"])
        self.logger.info("*****Selecting Day*******")
        self.SP.selectMonths(self.data["customer"]["months"])
        self.logger.info("*****Selecting Month*******")
        self.SP.selectYears(self.data["customer"]["years"])
        self.logger.info("*****Selecting Year*******")
        self.SP.clickNewsCbk()
        self.logger.info("*****Clicking on News Letter*****")
        self.SP.clickOffer()
        self.logger.info("*****Clicking on Offers*****")
        self.SP.setFirstName(random_name)
        self.logger.info("*****Setting First Name******")
        self.SP.setLastName(random_name)
        self.logger.info("*****Setting Last Name******")
        self.SP.setCompanyName(random_name)
        self.logger.info("*****Setting Company Name******")
        self.SP.setAddress1(random_email)
        self.logger.info("*****Setting Address1******")
        self.SP.setAddress2(random_email)
        self.logger.info("*****Setting Address2******")
        #self.SP.selectCountry("India")
        self.SP.selectCountry(self.data["customer"]["country"])
        self.logger.info("*****Selecting Country******")
        #self.SP.setState("TamilNadu")
        self.SP.setState(self.data["customer"]["state"])
        self.logger.info("*****Setting State Name******")
        #self.SP.setCity("Chennai")
        self.SP.setCity(self.data["customer"]["city"])
        self.logger.info("*****Setting City Name******")
        #self.SP.setZipCode("600001")
        self.SP.setZipCode(self.data["customer"]["zip_code"])
        self.logger.info("*****Setting Zip Code******")
        #self.SP.setMobileNumber("9912309123")
        self.SP.setMobileNumber(self.data["customer"]["mobile"])
        self.logger.info("*****Setting Mobile Number******")
        self.SP.clickCreateAcc()
        self.logger.info("*****Clicking on Create Account*******")
        self.AC = AccountCreatedPage(self.driver)
        self.AC.validatePageTitle()
        self.logger.info("*****Validating the Account Created Page Title*******")
        self.AC.validateAccountCreation()
        self.logger.info("*****Validating the Account Created Header*******")
        self.AC.validateSuccessMsg1()
        self.logger.info("*****Validating the Account Created Success Message1*******")
        self.AC.validateSuccessMsg2()
        self.logger.info("*****Validating the Account Created Success Message2*******")
        self.AC.clickContinueBtn()
        self.logger.info("*****Click on Continue Button*******")
        self.HP=HomePage(self.driver)
        self.HP.validate_loggedIn()
        self.logger.info("*****Validating Logged In details*******")
        self.HP.validateUserName(random_name)
        self.logger.info("*****Home Page Logged In User Info Validation******")
        self.HP.clickLogout()
        self.logger.info("*****Click on Home Page Logout Link******")
        # self.HP.validate_deleteAccount()
        # self.logger.info("*****Home Page Delete Account Link******")
