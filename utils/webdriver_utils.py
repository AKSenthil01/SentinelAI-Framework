from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException
)

from utils.self_healing import SelfHealing


class WebDriverUtils:

    @staticmethod
    def safe_click(driver, locator, timeout=20):

        wait = WebDriverWait(driver, timeout)

        # Use Self-Healing instead of Selenium directly
        element = SelfHealing.find(
            driver,
            wait,
            locator,
            EC.presence_of_element_located
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        try:

            WebDriverWait(driver, 5).until(
                lambda d: element.is_displayed() and element.is_enabled()
            )

            element.click()

        except (ElementClickInterceptedException, TimeoutException):

            driver.execute_script(
                "arguments[0].click();",
                element
            )