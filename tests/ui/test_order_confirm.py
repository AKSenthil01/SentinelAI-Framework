import allure
import pytest

from core.config import get_base_url

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
from utils.data_loader import load_test_data


@allure.epic("Enterprise Automation Framework")
@allure.feature("UI Order Flow")
@allure.story("Complete Order Placement")

@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.run(order=4)
class TestOrderConfirmation:

    logger = get_custom_logger(__name__)

    data = load_test_data()

    @allure.title("Complete Order Placement Workflow")
    @allure.description("""
    Register a new customer.

    Search products.

    Add products to cart.

    Checkout.

    Pay using card.

    Download invoice.

    Logout successfully.
    """)
    @allure.severity(allure.severity_level.CRITICAL)

    def test_order_confirm(
            self,
            setup,
            random_name,
            random_email,
            payment_data,
            reg_password
    ):
        with allure.step("Launch Application"):
            self.driver = setup

            self.driver.get(get_base_url())

            self.driver.maximize_window()

            self.HP = HomePage(self.driver)

            self.HP.validatePageTitle()

            self.logger.info("Application launched successfully")

        with allure.step("Register New Customer"):
            self.HP.clickLogin()

            self.AccReg = AccountRegistrationPage(self.driver)

            self.AccReg.validatePageTitle()

            self.AccReg.setName(random_name)

            self.AccReg.setEmail(random_email)

            self.AccReg.clickSignup()

        with allure.step("Complete Registration Form"):
            self.SP = SignUp(self.driver)

            self.SP.validatePageTitle()

            assert self.SP.validateInfo()

            self.SP.clickOnMr()

            self.SP.setPassword(reg_password)

            self.SP.selectDays(self.data["customer"]["days"])

            self.SP.selectMonths(self.data["customer"]["months"])

            self.SP.selectYears(self.data["customer"]["years"])

            self.SP.clickNewsCbk()

            self.SP.clickOffer()

            self.SP.setFirstName(random_name)

            self.SP.setLastName(random_name)

            self.SP.setCompanyName(random_name)

            self.SP.setAddress1(random_email)

            self.SP.setAddress2(random_email)

            self.SP.selectCountry(self.data["customer"]["country"])

            self.SP.setState(self.data["customer"]["state"])

            self.SP.setCity(self.data["customer"]["city"])

            self.SP.setZipCode(self.data["customer"]["zip_code"])

            self.SP.setMobileNumber(self.data["customer"]["mobile"])

            self.SP.clickCreateAcc()

        with allure.step("Verify Account Creation"):
            self.AC = AccountCreatedPage(self.driver)

            self.AC.validatePageTitle()

            self.AC.validateAccountCreation()

            self.AC.validateSuccessMsg1()

            self.AC.validateSuccessMsg2()

            self.AC.clickContinueBtn()

        with allure.step("Verify Home Page"):
            self.HP = HomePage(self.driver)

            assert self.HP.validate_loggedIn()

            self.HP.validate_logout()

            self.HP.validate_deleteAccount()

            self.HP.validate_featuresItems()

            self.HP.validateBrands()

            self.HP.validateCategoryItems()

            self.HP.validateRecommendedItems()

        with allure.step("Navigate to Products"):
            self.HP.clickProducts()

            self.Prod = AllProductsPage(self.driver)

            self.Prod.validatePageTitle()

            self.Prod.validateAllProducts()

            self.Prod.searchProduct(
                self.data["customer"]["product"]
            )

            self.Prod.validateSearchedProd()

        with allure.step("Add Products To Cart"):
            self.Prod.add_products_above_price(
                self.data["customer"]["price_threshold"]
            )

            self.Prod.clickOnCart()

        with allure.step("Checkout"):
            self.Cart = ShopingCartPage(self.driver)

            self.Cart.validatePageTitle()

            self.Cart.clickProceedToCheckout()

            self.CH = CheckoutPage(self.driver)

            self.CH.clickOnPlaceOrder()

        with allure.step("Complete Payment"):
            self.PP = PaymentPage(self.driver)

            self.PP.pay_with_card(

                name=payment_data["name"],

                number=payment_data["number"],

                cvc=payment_data["cvc"],

                month=payment_data["month"],

                year=payment_data["year"]

            )

        with allure.step("Verify Order Success"):
            self.DD = OrderPlacedPage(self.driver)

            self.DD.verify_order_success()

        with allure.step("Download Invoice"):
            self.DD.downloadInvoice()

            assert self.DD.verifyInvoiceDownloaded(

                "invoice.txt"

            ), "Invoice download failed."

        with allure.step("Logout"):
            self.DD.clickContinue()

            self.HP = HomePage(self.driver)

            self.HP.clickLogout()

            self.AccReg.validatePageTitle()

            self.logger.info(
                "Complete Order Workflow executed successfully."
            )