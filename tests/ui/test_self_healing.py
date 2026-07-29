import allure
import pytest

from core.config import get_base_url
from utils.customLogger import get_custom_logger
from utils.data_loader import load_test_data
from utils.healing_logger import HealingLogger

from pages.HomePage import HomePage
from pages.AccountRegistrationPage import AccountRegistrationPage
from pages.SignUpPage import SignUp
from pages.AccountCreatedPage import AccountCreatedPage
from pages.AllProductsPage import AllProductsPage
from pages.ShopingCartPage import ShopingCartPage
from pages.CheckOutPage import CheckoutPage
from pages.PaymentPage import PaymentPage
from pages.OrderPlacedPage import OrderPlacedPage


@allure.epic("Enterprise Automation Framework")
@allure.feature("Rule-Based Self-Healing")
@allure.story("Recover Broken Locator using Repository / Strategy / Fuzzy Matching")

@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.self_healing
@pytest.mark.run(order=5)
class TestSelfHealing:

    logger = get_custom_logger(__name__)
    data = load_test_data()

    @allure.title("Rule-Based Self-Healing Demo")
    @allure.description(
        """
        Demonstrates Rule-Based Self-Healing.

        Recovery order

        Repository
        ↓
        Strategy
        ↓
        Fuzzy Matching

        Repository is automatically updated after successful recovery.
        """
    )

    @allure.severity(allure.severity_level.CRITICAL)

    def test_self_healing(

            self,
            setup,
            random_name,
            random_email,
            payment_data,
            reg_password

    ):

        HealingLogger.clear()

        self.driver = setup

        self.driver.get(get_base_url())

        self.driver.maximize_window()

        #
        # Home Page
        #

        with allure.step("Open Home Page"):

            home = HomePage(self.driver)

            home.validatePageTitle()

        with allure.step("Navigate to Login"):

            home.clickLogin()

        #
        # Registration
        #

        with allure.step("Register New User"):

            registration = AccountRegistrationPage(self.driver)

            registration.validatePageTitle()

            registration.setName(random_name)

            registration.setEmail(random_email)

            registration.clickSignup()

        #
        # Signup
        #

        with allure.step("Complete Registration Form"):

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

        with allure.step("Verify Account Creation"):

            account = AccountCreatedPage(self.driver)

            account.clickContinueBtn()

        #
        # Products
        #

        with allure.step("Search Product"):

            home = HomePage(self.driver)

            home.clickProducts()

            products = AllProductsPage(self.driver)

            products.searchProduct(
                self.data["customer"]["product"]
            )

            products.add_products_above_price(
                self.data["customer"]["price_threshold"]
            )

            products.clickOnCart()

        #
        # Checkout
        #

        with allure.step("Proceed to Checkout"):

            cart = ShopingCartPage(self.driver)

            cart.clickProceedToCheckout()

            checkout = CheckoutPage(self.driver)

            checkout.clickOnPlaceOrder()

        #
        # Rule-Based Self-Healing Starts Here
        #

        with allure.step("Complete Payment"):

            payment = PaymentPage(self.driver)

            payment.pay_with_card(

                name=payment_data["name"],

                number=payment_data["number"],

                cvc=payment_data["cvc"],

                month=payment_data["month"],

                year=payment_data["year"]

            )

        #
        # Order Verification
        #

        with allure.step("Verify Order"):

            order = OrderPlacedPage(self.driver)

            order.verify_order_success()

            order.clickContinue()

        #
        # Logout
        #

        with allure.step("Logout"):

            home.clickLogout()