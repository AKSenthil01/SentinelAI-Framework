import allure
import pytest

from utils.allure_helper import AllureHelper
from utils.api.api_client import ApiClient
from utils.api.response_validator import ResponseValidator
from utils.api.api_logger import ApiLogger
from utils.data_generator.data_generator import DataGenerator

from pages.HomePage import HomePage
from pages.AccountRegistrationPage import AccountRegistrationPage
from pages.AllProductsPage import AllProductsPage
from pages.ShopingCartPage import ShopingCartPage
from pages.CheckOutPage import CheckoutPage
from pages.PaymentPage import PaymentPage
from pages.OrderPlacedPage import OrderPlacedPage


@pytest.mark.hybrid
@allure.epic("Enterprise Automation Framework")
@allure.feature("Hybrid Automation")
@allure.story("End-to-End Order Flow")
@allure.tag("Hybrid")
@allure.tag("API")
@allure.tag("UI")
@allure.tag("Regression")

@allure.label("owner", "A K Senthil Kumar")

@pytest.mark.hybrid
@pytest.mark.api
@pytest.mark.ui
@pytest.mark.run(order=7)
class TestHybridOrderFlow:

    @allure.title("Hybrid API + UI Order Flow")
    @allure.description(
        "Creates customer using API, performs UI login, adds products, places order, validates successful checkout."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_hybrid_order_flow(
            self,
            setup,
            test_data,
            payment_data
    ):

        # ==========================================================
        # STEP 1 : Create User through API
        # ==========================================================

        user = DataGenerator.create_user()

        import json

        with allure.step("Create User using API"):
            allure.attach(
                json.dumps(user, indent=4),
                name="Create User Request",
                attachment_type=allure.attachment_type.JSON
            )

            response = ApiClient.post(
                "/createAccount",
                data=user
            )

            allure.attach(
                response.text,
                name="Create User Response",
                attachment_type=allure.attachment_type.JSON
            )

            ResponseValidator.validate_status(response, 200)

            assert response.json()["responseCode"] == 201, \
                "API Create User failed."

            ApiLogger.logger.info(
                "✓ User created successfully through API"
            )
        # ==========================================================
        # STEP 2 : Open Website & Login through UI
        # ==========================================================

        with allure.step("Open Home Page"):
            home = HomePage(setup)
            home.openURL()
            home.validatePageTitle()

        with allure.step("Navigate to Login"):
            home.clickLogin()

            login = AccountRegistrationPage(setup)

            login.login(
                user["email"],
                user["password"]
            )

        assert home.validate_loggedIn()
        AllureHelper.attach_png(
            setup,
            "Logged In"
        )

        ApiLogger.logger.info("✓ User logged in successfully")

        # ==========================================================
        # STEP 3 : Navigate to Products
        # ==========================================================

        with allure.step("Search Product"):
            home.clickProducts()

            products = AllProductsPage(setup)

            products.searchProduct(
                test_data["customer"]["product"]
            )

            products.validateSearchedProd()

            AllureHelper.attach_png(
                setup,
                "Products Page"
            )

            ApiLogger.logger.info(
                "✓ Product searched successfully"
            )
        # ==========================================================
        # STEP 4 : Add Product to Cart
        # ==========================================================

        with allure.step("Add Products to Cart"):
            products.add_products_above_price(
                test_data["customer"]["price_threshold"]
            )

            products.clickOnCart()

            AllureHelper.attach_png(
                setup,
                "Cart"
            )

            ApiLogger.logger.info(
                "✓ Product added to cart"
            )
        # ==========================================================
        # STEP 5 : Checkout
        # ==========================================================

        with allure.step("Proceed to Checkout"):
            cart = ShopingCartPage(setup)

            cart.clickProceedToCheckout()

            checkout = CheckoutPage(setup)

            checkout.clickOnPlaceOrder()

            AllureHelper.attach_png(
                setup,
                "Checkout"
            )

            ApiLogger.logger.info(
                "✓ Proceeded to Checkout"
            )

        # ==========================================================
        # STEP 6 : Payment
        # ==========================================================

        with allure.step("Complete Payment"):
            payment = PaymentPage(setup)

            payment.pay_with_card(

                name=payment_data["name"],

                number=payment_data["number"],

                cvc=payment_data["cvc"],

                month=payment_data["month"],

                year=payment_data["year"]

            )

            AllureHelper.attach_png(
                setup,
                "Payment Success"
            )

            ApiLogger.logger.info(
                "✓ Payment completed successfully"
            )
        # ==========================================================
        # STEP 7 : Verify Order
        # ==========================================================

        with allure.step("Verify Order"):
            order = OrderPlacedPage(setup)

            order.verify_order_success()

            AllureHelper.attach_png(
                setup,
                "Order Success"
            )

            ApiLogger.logger.info(
                "✓ Order placed successfully"
            )
        # ==========================================================
        # STEP 8 : Delete User through API
        # ==========================================================

        with allure.step("Delete User using API"):
            payload = {
                "email": user["email"],
                "password": user["password"]
            }

            allure.attach(
                json.dumps(payload, indent=4),
                name="Delete User Request",
                attachment_type=allure.attachment_type.JSON
            )

            response = ApiClient.delete(
                "/deleteAccount",
                data=payload
            )

            allure.attach(
                response.text,
                name="Delete User Response",
                attachment_type=allure.attachment_type.JSON
            )

            ResponseValidator.validate_status(response, 200)

            assert response.json()["responseCode"] == 200, \
                "API Delete User failed."

            ApiLogger.logger.info(
                "✓ User deleted successfully"
            )