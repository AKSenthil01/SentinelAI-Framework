import allure
import pytest

from core.config import get_base_url

from pages.AccountRegistrationPage import AccountRegistrationPage
from pages.HomePage import HomePage

from utils.customLogger import get_custom_logger
from utils.data_loader import load_test_data


@allure.epic("Enterprise Automation Framework")
@allure.feature("User Authentication")
@allure.story("Login Existing User")

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.run(order=2)
class TestLogin:
    logger = get_custom_logger(__name__)

    data = load_test_data()

    @allure.title("Login Existing Customer")
    @allure.description(
        """
        Login using an existing customer account,
        verify successful login,
        logout,
        and verify the Login page is displayed again.
        """
    )
    @allure.severity(allure.severity_level.CRITICAL)

    def test_login(
            self,
            setup,
            existing_user,
            reg_password
    ):

        self.logger.info("========== Test002Login Started ==========")

        self.driver = setup

        #
        # Launch Application
        #

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
                f"User logged in successfully : {existing_user}"
            )

        #
        # Verify Login
        #

        with allure.step("Verify Logged-in User"):

            self.HP = HomePage(self.driver)

            assert self.HP.validate_loggedIn(), \
                "Logged-in user information not displayed."

            self.logger.info("Login verified successfully")

        #
        # Logout
        #

        with allure.step("Logout from Application"):

            self.HP.clickLogout()

            self.logger.info("User logged out successfully")

        #
        # Verify Login Page
        #

        with allure.step("Verify Login Page After Logout"):

            self.AccReg = AccountRegistrationPage(self.driver)

            self.AccReg.validatePageTitle()

            self.logger.info(
                "Login page displayed after logout"
            )

        self.logger.info(
            "========== Test002Login Completed Successfully =========="
        )