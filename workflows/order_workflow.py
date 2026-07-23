from pages.HomePage import HomePage
from pages.AccountRegistrationPage import AccountRegistrationPage
from pages.AllProductsPage import AllProductsPage
from pages.ShopingCartPage import ShopingCartPage
from pages.CheckOutPage import CheckOutPage
from pages.PaymentPage import PaymentPage
from pages.OrderPlacedPage import OrderPlacedPage


class OrderWorkflow:

    def __init__(self, driver, test_data):

        self.driver = driver
        self.data = test_data

    # ----------------------------------------------------

    def login(self, email, password):

        home = HomePage(self.driver)

        home.clickLogin()

        login = AccountRegistrationPage(self.driver)

        login.login(

            email,

            password

        )

        assert home.validate_loggedIn()

        return self

    # ----------------------------------------------------

    def purchase_product(self):

        home = HomePage(self.driver)

        home.clickProducts()

        products = AllProductsPage(self.driver)

        products.searchProduct(

            self.data["customer"]["product"]

        )

        products.validateSearchedProd()

        products.add_products_above_price(

            self.data["customer"]["price_threshold"]

        )

        products.clickOnCart()

        cart = ShopingCartPage(self.driver)

        cart.clickProceedToCheckout()

        checkout = CheckOutPage(self.driver)

        checkout.placeOrder()

        payment = PaymentPage(self.driver)

        payment.pay_with_card(

            self.data["customer"]["name"],

            self.data["payment"]["card_number"],

            self.data["payment"]["cvc"],

            self.data["payment"]["month"],

            self.data["payment"]["year"]

        )

        order = OrderPlacedPage(self.driver)

        order.verify_order_success()

        return self