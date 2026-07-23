import pytest

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
class TestHybridOrderFlow:

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

        response = ApiClient.post(
            "/createAccount",
            data=user
        )

        ResponseValidator.validate_status(response, 200)
        assert response.json()["responseCode"] == 201

        ApiLogger.logger.info("✓ User created successfully through API")

        # ==========================================================
        # STEP 2 : Open Website & Login through UI
        # ==========================================================

        home = HomePage(setup)

        # IMPORTANT
        home.openURL()      # <-- This was missing

        home.clickLogin()

        login = AccountRegistrationPage(setup)

        login.login(
            user["email"],
            user["password"]
        )

        assert home.validate_loggedIn()

        ApiLogger.logger.info("✓ User logged in successfully")

        # ==========================================================
        # STEP 3 : Navigate to Products
        # ==========================================================

        home.clickProducts()

        products = AllProductsPage(setup)

        products.searchProduct(
            test_data["customer"]["product"]
        )

        products.validateSearchedProd()

        ApiLogger.logger.info("✓ Product searched successfully")

        # ==========================================================
        # STEP 4 : Add Product to Cart
        # ==========================================================

        products.add_products_above_price(
            test_data["customer"]["price_threshold"]
        )

        products.clickOnCart()

        ApiLogger.logger.info("✓ Product added to cart")

        # ==========================================================
        # STEP 5 : Checkout
        # ==========================================================

        cart = ShopingCartPage(setup)

        cart.clickProceedToCheckout()

        checkout = CheckoutPage(setup)

        checkout.clickOnPlaceOrder()

        ApiLogger.logger.info("✓ Proceeded to Checkout")

        # ==========================================================
        # STEP 6 : Payment
        # ==========================================================

        payment = PaymentPage(setup)

        payment.pay_with_card(
            name=payment_data["name"],
            number=payment_data["number"],
            cvc=payment_data["cvc"],
            month=payment_data["month"],
            year=payment_data["year"]
        )

        ApiLogger.logger.info("✓ Payment completed successfully")

        # ==========================================================
        # STEP 7 : Verify Order
        # ==========================================================

        order = OrderPlacedPage(setup)

        order.verify_order_success()

        ApiLogger.logger.info("✓ Order placed successfully")

        # ==========================================================
        # STEP 8 : Delete User through API
        # ==========================================================

        response = ApiClient.delete(
            "/deleteAccount",
            data={
                "email": user["email"],
                "password": user["password"]
            }
        )

        ResponseValidator.validate_status(response, 200)
        assert response.json()["responseCode"] == 200

        ApiLogger.logger.info("✓ User deleted successfully")