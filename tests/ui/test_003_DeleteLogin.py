import logging
import time

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


class Test003DeleteLogin:
    logger = get_custom_logger(__name__)
    data = load_test_data()

    def test_DelLogin(self, setup, existing_user ,reg_password):
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
        # #self.driver.implicitly_wait(10)
        # self.AccReg.validatePageTitle()
        # self.logger.info("*****Validating Account Registration Page Title*****")
        # #self.AccReg.clickOnAd()
        # self.logger.info("*****Entering user name and password on Registration page*****")
        # #self.AccReg.setName(random_name)
        self.AccReg.setUserEmail(existing_user)
        self.AccReg.setPassword(reg_password)
        self.AccReg.clickLogin()
        self.logger.info("*****Clicking on Login Button*****")
        #time.sleep(10)
        self.HP=HomePage(self.driver)
        #self.HP.validate_loggedIn()
        # # self.logger.info("*****Validating Logged In details*******")
        # # self.HP.validateUserName(random_name)
        # # self.logger.info("*****Home Page Logged In User Info Validation******")
        self.HP.deleteAccount()
        self.logger.info("*****Click on Delete Account Link******")
        # # self.HP.validate_deleteAccount()
        # # self.logger.info("*****Home Page Delete Account Link******")
        self.AC=AccountCreatedPage(self.driver)
        self.AC.validatePageTitle()
        self.logger.info("*****Validating Account Delete Page Title*****")
        self.AC.validatePageTitle()
        self.logger.info("*****Validating Account Delete Message*****")
        self.AC.validateDeleteMsg1()
        self.logger.info("*****Validating Delete Message1*****")
        self.AC.validateDeleteMsg2()
        self.logger.info("*****Validating Delete Message2*****")
        self.AC.clickContinueBtn()
        self.logger.info("*****Click on Continue Button*****")
        self.HP = HomePage(self.driver)
        self.HP.validatePageTitle()


