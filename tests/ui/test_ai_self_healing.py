
import json
import os
import allure
import pytest

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
from utils.ai.ai_session import AISession
from utils.allure_helper import AllureHelper
from utils.customLogger import get_custom_logger
from utils.data_loader import load_test_data
from utils.healing_logger import HealingLogger


@allure.epic("Enterprise Automation Framework")
@allure.feature("AI Self-Healing")
@allure.story("Recover Broken Locator Using Ollama")

@pytest.mark.ui
@pytest.mark.ai
@pytest.mark.run(order=6)
class TestAISelfHealing:
    logger = get_custom_logger(__name__)
    data = load_test_data()

    @allure.title("AI Self-Healing Demo")
    @allure.description(
        "Demonstrates AI-based locator recovery using Ollama and updates the locator repository."
    )

    def test_ai_self_healing(
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
        # Home
        #

        with allure.step("Open Home Page"):
            hp = HomePage(self.driver)
            hp.validatePageTitle()

            AllureHelper.attach_png(
                self.driver,
                "01 - Home Page"
            )

        with allure.step("Navigate to Login"):
            hp.clickLogin()

        #
        # Registration
        #
        with allure.step("Register New User"):
            reg = AccountRegistrationPage(self.driver)

            reg.validatePageTitle()

            reg.setName(random_name)

            reg.setEmail(random_email)

            reg.clickSignup()

        #
        # Signup
        #
        with allure.step("Signup New User"):
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

            AllureHelper.attach_png(
                self.driver,
                "02 - Registration Completed"
            )

        #
        # Account Created
        #
        with allure.step("Account Created Page"):
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
        with allure.step("Search and Add Products"):
            prod = AllProductsPage(self.driver)

            prod.searchProduct(
            self.data["customer"]["product"]
            )

            prod.add_products_above_price(
            self.data["customer"]["price_threshold"]
            )

            prod.clickOnCart()

            AllureHelper.attach_png(
                self.driver,
                "03 - Shopping Cart"
            )

        #
        # Cart
        #
        with allure.step("Checkout"):
            cart = ShopingCartPage(self.driver)

            cart.clickProceedToCheckout()

            checkout = CheckoutPage(self.driver)

            checkout.clickOnPlaceOrder()

            AllureHelper.attach_png(
                self.driver,
                "04 - Checkout"
            )

        #
        # **********************
        # AI SELF HEALING STARTS HERE
        # **********************
        #
        with allure.step("AI Self-Healing Payment"):
            payment = PaymentPageAIDemo(self.driver)

            payment.pay_with_card(

            name=payment_data["name"],

            number=payment_data["number"],

            cvc=payment_data["cvc"],

            month=payment_data["month"],

            year=payment_data["year"]

            )

            AllureHelper.attach_png(
                self.driver,
                "05 - AI Self Healing Success"
            )

            AllureHelper.attach_json(
                "reports/healing_log.json",
                "Healing Log"
            )

            AllureHelper.attach_json(
                "repository/locator_repository.json",
                "Locator Repository"
            )

            AllureHelper.attach_html(
                "reports/healing_dashboard.html",
                "Healing Dashboard"
            )


        with allure.step("Verify Order Successfully Placed"):

            order = OrderPlacedPage(self.driver)

        # order.downloadInvoice()
        #
        # assert order.verifyInvoiceDownloaded(
        #     "invoice.txt"
        # )

            order.verify_order_success()

            AllureHelper.attach_png(
                self.driver,
                "06 - Order Successfully Placed"
            )

            AllureHelper.attach_png(
                self.driver,
                "Order Completed"
            )

        with allure.step("Return to Home"):

            order.clickContinue()

        with allure.step("Logout"):

            hp.clickLogout()

            AllureHelper.attach_png(
                self.driver,
                "Logout"
            )

            AllureHelper.attach_json(
                "reports/healing_log.json",
                "Healing Log"
            )

            AllureHelper.attach_json(
                "repository/locator_repository.json",
                "Locator Repository"
            )

            AllureHelper.attach_html(
                "reports/healing_dashboard.html",
                "Healing Dashboard"
            )

            AllureHelper.attach_prompt(
                AISession.last_prompt
            )

            AllureHelper.attach_response(
                AISession.last_response
            )


