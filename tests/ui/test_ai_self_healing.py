import json
import os

from pages.AccountCreatedPage import AccountCreatedPage
from pages.AccountRegistrationPage import AccountRegistrationPage
from pages.AllProductsPage import AllProductsPage
from pages.CheckOutPage import CheckoutPage
from pages.HomePage import HomePage
from pages.OrderPlacedPage import OrderPlacedPage
from pages.PaymentPageAIDemo import PaymentPageAIDemo
from pages.ShopingCartPage import ShopingCartPage
from pages.SignUpPage import SignUp

from core.config import get_base_url
from utils.customLogger import get_custom_logger
from utils.data_loader import load_test_data
from utils.healing_logger import HealingLogger


class TestAISelfHealing:

    logger = get_custom_logger(__name__)
    data = load_test_data()

    def test_ai_self_healing(
            self,
            setup,
            random_name,
            random_email,
            payment_data,
            reg_password
    ):

        #
        # Force Repository Empty
        #

        # repo = "locator_repository.json"
        #
        # if os.path.exists(repo):
        #
        #     with open(repo, "w") as f:
        #         json.dump({}, f, indent=4)

        #
        # Clear healing log
        #

        HealingLogger.clear()

        self.driver = setup

        self.driver.get(get_base_url())

        self.driver.maximize_window()

        #
        # Home
        #

        hp = HomePage(self.driver)

        hp.validatePageTitle()

        hp.clickLogin()

        #
        # Registration
        #

        reg = AccountRegistrationPage(self.driver)

        reg.validatePageTitle()

        reg.setName(random_name)

        reg.setEmail(random_email)

        reg.clickSignup()

        #
        # Signup
        #

        signup = SignUp(self.driver)

        signup.validatePageTitle()

        signup.clickOnMr()

        signup.setPassword(reg_password)

        signup.selectDays(
            self.data["customer"]["days"]
        )

        signup.selectMonths(
            self.data["customer"]["months"]
        )

        signup.selectYears(
            self.data["customer"]["years"]
        )

        signup.clickNewsCbk()

        signup.clickOffer()

        signup.setFirstName(random_name)

        signup.setLastName(random_name)

        signup.setCompanyName(random_name)

        signup.setAddress1(random_email)

        signup.setAddress2(random_email)

        signup.selectCountry(
            self.data["customer"]["country"]
        )

        signup.setState(
            self.data["customer"]["state"]
        )

        signup.setCity(
            self.data["customer"]["city"]
        )

        signup.setZipCode(
            self.data["customer"]["zip_code"]
        )

        signup.setMobileNumber(
            self.data["customer"]["mobile"]
        )

        signup.clickCreateAcc()

        #
        # Account Created
        #

        ac = AccountCreatedPage(self.driver)

        ac.clickContinueBtn()

        #
        # Home
        #

        hp = HomePage(self.driver)

        hp.clickProducts()

        #
        # Products
        #

        prod = AllProductsPage(self.driver)

        prod.searchProduct(
            self.data["customer"]["product"]
        )

        prod.add_products_above_price(
            self.data["customer"]["price_threshold"]
        )

        prod.clickOnCart()

        #
        # Cart
        #

        cart = ShopingCartPage(self.driver)

        cart.clickProceedToCheckout()

        #
        # Checkout
        #

        checkout = CheckoutPage(self.driver)

        checkout.clickOnPlaceOrder()

        #
        # **********************
        # AI SELF HEALING STARTS HERE
        # **********************
        #

        payment = PaymentPageAIDemo(self.driver)

        payment.pay_with_card(

            name=payment_data["name"],

            number=payment_data["number"],

            cvc=payment_data["cvc"],

            month=payment_data["month"],

            year=payment_data["year"]

        )

        #
        # Order Placed
        #

        order = OrderPlacedPage(self.driver)

        order.downloadInvoice()

        assert order.verifyInvoiceDownloaded(
            "invoice.txt"
        )

        order.clickContinue()

        hp.clickLogout()