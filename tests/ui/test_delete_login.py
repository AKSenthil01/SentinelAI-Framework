import allure
import pytest

from core.config import get_base_url

from pages.AccountCreatedPage import AccountCreatedPage
from pages.AccountRegistrationPage import AccountRegistrationPage
from pages.HomePage import HomePage

from utils.customLogger import get_custom_logger
from utils.data_loader import load_test_data


@allure.epic("Enterprise Automation Framework")
@allure.feature("User Account")
@allure.story("Delete Existing User")

@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.run(order=3)
class TestDeleteLogin:

    logger = get_custom_logger(__name__)

    data = load_test_data()

    @allure.title("Delete Existing User Account")
    @allure.description(
        """
        Login using an existing customer account,
        delete the account,
        verify the Account Deleted page,
        and return to the Home page.
        """
    )
    @allure.severity(allure.severity_level.CRITICAL)

    def test_delete_login(
            self,
            setup,
            existing_user,
            reg_password
    ):

        self.logger.info("========== Delete Account Test Started ==========")

        self.driver = setup

        #
        # Launch Application
        #

        with allure.step("Launch Application"):

            self.driver.get(get_base_url())

            self.driver.maximize_window()

            self.logger.info("Application launched")

        #
        # Home Page
        #

        with allure.step("Validate Home Page"):

            self.HP = HomePage(self.driver)

            self.HP.validatePageTitle()

            self.logger.info("Home page validated")

        #
        # Login Page
        #

        with allure.step("Navigate to Login Page"):

            self.HP.clickLogin()

            self.logger.info("Login page opened")

        #
        # Login
        #

        with allure.step("Login with Existing User"):

            self.AccReg = AccountRegistrationPage(self.driver)

            self.AccReg.validatePageTitle()

            self.AccReg.setUserEmail(existing_user)

            self.AccReg.setPassword(reg_password)

            self.AccReg.clickLogin()

            self.logger.info(
                f"Logged in successfully : {existing_user}"
            )

        #
        # Verify Login
        #

        with allure.step("Verify Logged-in User"):

            self.HP = HomePage(self.driver)

            assert self.HP.validate_loggedIn(), \
                "User login verification failed."

            self.logger.info("Login verified")

        #
        # Delete Account
        #

        with allure.step("Delete User Account"):

            self.HP.deleteAccount()

            self.logger.info("Delete Account clicked")

        #
        # Account Deleted Page
        #

        with allure.step("Validate Account Deleted Page"):

            self.AC = AccountCreatedPage(self.driver)

            self.AC.validatePageTitle()

            self.AC.validateDeleteMsg1()

            self.AC.validateDeleteMsg2()

            self.logger.info("Account Deleted page validated")

        #
        # Continue
        #

        with allure.step("Return to Home Page"):

            self.AC.clickContinueBtn()

            self.logger.info("Continue button clicked")

        #
        # Home Page
        #

        with allure.step("Verify Home Page"):

            self.HP = HomePage(self.driver)

            self.HP.validatePageTitle()

            self.logger.info("Returned to Home Page")

        self.logger.info(
            "========== Delete Account Test Completed Successfully =========="
        )