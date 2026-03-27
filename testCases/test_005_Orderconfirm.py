import logging

from pageObjects.AccountCreatedPage import AccountCreatedPage
#from venv import logger

from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.AllProductsPage import AllProductsPage
from pageObjects.CheckOutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from pageObjects.OrderPlacedPage import OrderPlacedPage
from pageObjects.PaymentPage import PaymentPage
from pageObjects.ShopingCartPage import ShopingCartPage
from pageObjects.ShopingPage import ShopingPage
from pageObjects.SignUpPage import SignUp
from utilities.customLogger import get_custom_logger





class Test001AccountReg:
    baseURL="https://automationexercise.com/"
    #logger=LogGen.loggen()
    logger = get_custom_logger(__name__)

    def test_AccountReg(self, setup, random_name, random_email , payment_data):
        self.logger.info("*****test_001_AccountRegistration started*****")
    #    self.logger.setLevel(logging.DEBUG)
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("*****Launching Application*****")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.HP=HomePage(self.driver)
        self.HP.validatePageTitle()
        self.logger.info("*****Validating Home Page Title*****")
        self.HP.clickLogin()
        self.logger.info("*****Clicking on Login link*****")
        self.driver.implicitly_wait(10)
        self.AccReg=AccountRegistrationPage(self.driver)
        self.driver.implicitly_wait(10)
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

        print(self.msg)
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
        self.SP.setPassword("Senpass77")
        self.logger.info("*****Setting Password*******")
        self.SP.selectDays("1")
        self.logger.info("*****Selecting Day*******")
        self.SP.selectMonths("1")
        self.logger.info("*****Selecting Month*******")
        self.SP.selectYears("1990")
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
        self.SP.selectCountry("India")
        self.logger.info("*****Selecting Country******")
        self.SP.setState("TamilNadu")
        self.logger.info("*****Setting State Name******")
        self.SP.setCity("Chennai")
        self.logger.info("*****Setting City Name******")
        self.SP.setZipCode("600001")
        self.logger.info("*****Setting Zip Code******")
        self.SP.setMobileNumber("9912309123")
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
        #self.HP.cleanUrl()
        self.HP.validate_loggedIn()
        self.logger.info("*****Home Page Logged In Info******")
        self.HP.validate_logout()
        self.logger.info("*****Home Page Logout Link******")
        self.HP.validate_deleteAccount()
        self.logger.info("*****Home Page Delete Account Link******")
        self.HP.validate_featuresItems()
        self.logger.info("*****Home Page Features Items Section******")
        self.HP.validateBrands()
        self.logger.info("*****Home Page Brands Section ******")
        self.HP.validateCategoryItems()
        self.logger.info("*****Home Page Category Item Section ******")
        self.HP.validateRecommendedItems()
        self.logger.info("*****Home Page Recommended Items Section ******")
        self.HP.validateProductsLnk()
        self.logger.info("*****Home Page Products Link Validation******")
        self.HP.clickProducts()
        self.logger.info("*****Home Page Click on Products Link ******")
        self.Prod = AllProductsPage(self.driver)
        self.Prod.validatePageTitle()
        self.logger.info("*****Validate All Products Page Title ******")
        self.Prod.validateAllProducts()
        self.logger.info("*****Validate All Products section ******")
        self.Prod.searchProduct()
        self.logger.info("*****Search a Product******")
        self.Prod.validateSearchedProd()
        self.logger.info("*****Validate Searched Product section ******")
        self.Prod.add_products_above_price(500)
        self.logger.info("*****Add Products whose price is > Rs.500 to the cart ******")
        self.Prod.clickOnCart()
        self.logger.info("*****Click on View Cart Link******")
        self.Cart=ShopingCartPage(self.driver)
        self.Cart.validatePageTitle()
        self.logger.info("*****Validate Shoping Cart Page Title******")
        self.Cart.clickProceedToCheckout()
        self.logger.info("*****Proceed to Checkout******")
        self.CH=CheckoutPage(self.driver)
        self.CH.clickOnPlaceOrder()
        self.logger.info("*****Place Order******")
        self.PP=PaymentPage(self.driver)
        self.PP.pay_with_card(
            name=payment_data["name"],
            number=payment_data["number"],
            cvc=payment_data["cvc"],
            month=payment_data["month"],
            year=payment_data["year"]
        )
        self.DD=OrderPlacedPage(self.driver)
        self.DD.downloadInvoice()
        self.logger.info("*****Download Invoice******")
        self.is_present=self.DD.verifyInvoiceDownloaded("invoice.txt")
        assert self.is_present, "The invoice file was not found in the downloads folder!"
        self.logger.info("*****Verify Invoice******")
        self.DD.clickContinue()
        self.logger.info("*****Click on Continue Button******")
        self.HP.validatePageTitle()
        self.logger.info("*****Validating Home Page Title*****")
        self.HP.clickLogout()
        self.logger.info("*****Click on Logout Link******")
        self.AccReg.validatePageTitle()
        self.logger.info("*****Validate Account Registration Page Title******")






















