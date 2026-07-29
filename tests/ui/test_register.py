import allure
import pytest

from core.config import get_base_url

from pages.AccountCreatedPage import AccountCreatedPage
from pages.AccountRegistrationPage import AccountRegistrationPage
from pages.HomePage import HomePage
from pages.SignUpPage import SignUp

from utils.customLogger import get_custom_logger
from utils.data_loader import load_test_data



@allure.epic("Enterprise Automation Framework")
@allure.feature("User Registration")
@allure.story("Register New Customer")

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.run(order=1)
class TestRegister:
    logger = get_custom_logger(__name__)

    data = load_test_data()

    @allure.title("Register New Customer")
    @allure.description(
        """
        Register a brand-new customer in Automation Exercise,
        verify successful account creation,
        validate logged-in username,
        and logout successfully.
        """
    )
    @allure.severity(allure.severity_level.CRITICAL)

    def test_register(
            self,
            setup,
            random_name,
            random_email,
            reg_password
    ):

        self.logger.info("========== Test001Register Started ==========")

        self.driver = setup

        with allure.step("Launch Application"):

            self.driver.get(get_base_url())

            self.driver.maximize_window()

            self.logger.info("Application launched successfully")

        #
        # Home Page
        #

        with allure.step("Validate Home Page"):

            self.HP = HomePage(self.driver)

            self.HP.validatePageTitle()

            self.logger.info("Home page validated successfully")

        with allure.step("Navigate to Login Page"):

            self.HP.clickLogin()

            self.logger.info("Navigated to Login page")

        #
        # Registration Page
        #

        with allure.step("Register New Customer"):

            self.AccReg = AccountRegistrationPage(self.driver)

            self.AccReg.validatePageTitle()

            self.AccReg.setName(random_name)

            self.AccReg.setEmail(random_email)

            self.AccReg.clickSignup()

            self.logger.info(
                f"Customer registration initiated for {random_email}"
            )

        #
        # Signup Page
        #

        with allure.step("Validate Signup Page"):

            self.SP = SignUp(self.driver)

            self.SP.validatePageTitle()

            assert self.SP.validateInfo(), \
                "Signup information message not displayed."

            self.logger.info("Signup page validated successfully")

        #
        # Complete Registration Form
        #

        with allure.step("Complete Customer Registration Form"):

            self.SP.clickOnMr()

            self.SP.setPassword(reg_password)

            self.SP.selectDays(
                self.data["customer"]["days"]
            )

            self.SP.selectMonths(
                self.data["customer"]["months"]
            )

            self.SP.selectYears(
                self.data["customer"]["years"]
            )

            self.SP.clickNewsCbk()

            self.SP.clickOffer()

            self.SP.setFirstName(random_name)

            self.SP.setLastName(random_name)

            self.SP.setCompanyName(random_name)

            self.SP.setAddress1(random_email)

            self.SP.setAddress2(random_email)

            self.SP.selectCountry(
                self.data["customer"]["country"]
            )

            self.SP.setState(
                self.data["customer"]["state"]
            )

            self.SP.setCity(
                self.data["customer"]["city"]
            )

            self.SP.setZipCode(
                self.data["customer"]["zip_code"]
            )

            self.SP.setMobileNumber(
                self.data["customer"]["mobile"]
            )

            self.logger.info(
                "Customer registration form completed successfully"
            )

        #
        # Create Account
        #

        with allure.step("Create Customer Account"):

            self.SP.clickCreateAcc()

            self.logger.info("Create Account button clicked")

        #
        # Account Created Page
        #

        with allure.step("Verify Account Created Successfully"):

            self.AC = AccountCreatedPage(self.driver)

            self.AC.validatePageTitle()

            assert self.AC.validateAccountCreation(), \
                "Account Created header not displayed."

            assert self.AC.validateSuccessMsg1(), \
                "Account creation success message-1 not displayed."

            assert self.AC.validateSuccessMsg2(), \
                "Account creation success message-2 not displayed."

            self.logger.info(
                "Customer account created successfully"
            )

        #
        # Continue
        #

        with allure.step("Continue to Home Page"):

            self.AC.clickContinueBtn()

            self.logger.info(
                "Continue button clicked"
            )

        #
        # Verify Home Page
        #

        with allure.step("Verify Logged-in User"):

            self.HP = HomePage(self.driver)

            assert self.HP.validate_loggedIn(), \
                "Logged-in user information was not displayed."

            self.logger.info(
                "User login verified successfully"
            )

        with allure.step("Verify Logged-in Username"):

            self.HP.validateUserName(random_name)

            self.logger.info(
                f"Logged in as : {random_name}"
            )

        #
        # Logout
        #

        with allure.step("Logout from Application"):

            self.HP.clickLogout()

            self.logger.info(
                "User logged out successfully"
            )

        #
        # Verify Login Page Again
        #

        with allure.step("Verify Login Page After Logout"):

            self.AccReg = AccountRegistrationPage(self.driver)

            self.AccReg.validatePageTitle()

            self.logger.info(
                "Login page displayed after logout"
            )

        self.logger.info(
            "========== Test001Register Completed Successfully =========="
        )