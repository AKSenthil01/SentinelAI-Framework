from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException
)
from utils.self_healing import SelfHealing
from utils.click_helper import ClickHelper


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # -----------------------------

    def find(self, *locator):

        # Supports:
        # self.find(locator)
        # self.find(By.ID, "username")

        if len(locator) == 1:
            locator = locator[0]

        elif len(locator) == 2:
            locator = (locator[0], locator[1])

        else:
            raise ValueError(f"Invalid locator: {locator}")

        return SelfHealing.find(
            self.driver,
            self.wait,
            locator,
            EC.presence_of_element_located
        )

    # -----------------------------

    def click(self, *locator):

        if len(locator) == 1:
            locator = locator[0]
        elif len(locator) == 2:
            locator = (locator[0], locator[1])
        else:
            raise ValueError(f"Invalid locator: {locator}")

        element = SelfHealing.find(
            self.driver,
            self.wait,
            locator,
            EC.element_to_be_clickable
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        try:

            ClickHelper.click(
                self.driver,
                element
            )

        except (ElementClickInterceptedException, TimeoutException):

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    # -----------------------------

    def inputText(self, locator, value):

        if len(locator) == 1:
            locator = locator[0]
        elif len(locator) == 2:
            locator = (locator[0], locator[1])
        else:
            raise ValueError(f"Invalid locator: {locator}")

        element = SelfHealing.find(
            self.driver,
            self.wait,
            locator,
            EC.visibility_of_element_located
        )

        element.clear()
        element.send_keys(value)

    # -----------------------------

    def getText(self, *locator):

        if len(locator) == 1:
            locator = locator[0]
        elif len(locator) == 2:
            locator = (locator[0], locator[1])
        else:
            raise ValueError(f"Invalid locator: {locator}")

        return SelfHealing.find(
            self.driver,
            self.wait,
            locator,
            EC.visibility_of_element_located
        ).text

    # -----------------------------

    def isDisplayed(self, *locator):

        if len(locator) == 1:
            locator = locator[0]
        elif len(locator) == 2:
            locator = (locator[0], locator[1])
        else:
            raise ValueError(f"Invalid locator: {locator}")

        return SelfHealing.find(
            self.driver,
            self.wait,
            locator,
            EC.visibility_of_element_located
        ).is_displayed()

    # -----------------------------

    def find_all(self, *locator):

        if len(locator) == 1:
            locator = locator[0]

        elif len(locator) == 2:
            locator = (locator[0], locator[1])

        else:
            raise ValueError(f"Invalid locator: {locator}")

        return SelfHealing.find_all(
            self.driver,
            self.wait,
            locator
        )

    #--------------------------------

    def clickElement(self, *locator):
        if len(locator) == 1:
            locator = locator[0]
        elif len(locator) == 2:
            locator = (locator[0], locator[1])
        else:
            raise ValueError(f"Invalid locator: {locator}")
        self.click(locator)

    # --------------------------------

    def validateMsg(self, *locator):
        if len(locator) == 1:
            locator = locator[0]
        elif len(locator) == 2:
            locator = (locator[0], locator[1])
        else:
            raise ValueError(f"Invalid locator: {locator}")
        return self.getText(locator)

    # --------------------------------

    def getElements(self, *locator):
        if len(locator) == 1:
            locator = locator[0]
        elif len(locator) == 2:
            locator = (locator[0], locator[1])
        else:
            raise ValueError(f"Invalid locator: {locator}")
        return self.find_all(locator)

    # --------------------------------

    def click_and_bypass(self, *locator):
        if len(locator) == 1:
            locator = locator[0]
        elif len(locator) == 2:
            locator = (locator[0], locator[1])
        else:
            raise ValueError(f"Invalid locator: {locator}")

        element = SelfHealing.find(
            self.driver,
            self.wait,
            locator,
            EC.presence_of_element_located
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # --------------------------------

    def scroll_to_and_click(self, *locator):
        if len(locator) == 1:
            locator = locator[0]
        elif len(locator) == 2:
            locator = (locator[0], locator[1])
        else:
            raise ValueError(f"Invalid locator: {locator}")

        element = SelfHealing.find(
            self.driver,
            self.wait,
            locator,
            EC.element_to_be_clickable
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        try:
            ClickHelper.click(
                self.driver,
                element
            )

        except (ElementClickInterceptedException, TimeoutException):
            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    # --------------------------------

    def page_title(self):
        return self.driver.title

    # --------------------------------

    def clearText(self, *locator):
        if len(locator) == 1:
            locator = locator[0]
        elif len(locator) == 2:
            locator = (locator[0], locator[1])
        else:
            raise ValueError(f"Invalid locator: {locator}")

        self.find(locator).clear()

    # --------------------------------

    def getAttribute(self, locator, attribute):

        return self.find(locator).get_attribute(attribute)

    # --------------------------------

    def isEnabled(self, locator):

        return self.find(locator).is_enabled()

    # --------------------------------

    def isSelected(self, locator):

        return self.find(locator).is_selected()

    # --------------------------------

    def wait_until_visible(self, locator):

        return SelfHealing.find(
            self.driver,
            self.wait,
            locator,
            EC.visibility_of_element_located
        )

    # --------------------------------
