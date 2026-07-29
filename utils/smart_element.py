"""
SmartElement

Thin wrapper over Selenium.

Every click/send_keys/get_text automatically
uses the SelfHealing engine.
"""

from selenium.webdriver.support import expected_conditions as EC

from utils.self_healing import SelfHealing


class SmartElement:

    def __init__(self, driver, wait, locator):
        self.driver = driver
        self.wait = wait
        self.locator = locator

    # ------------------------------------

    def _find(self):

        return SelfHealing.find_element(
            driver=self.driver,
            wait=self.wait,
            locator=self.locator,
            condition=EC.presence_of_element_located
        )

    # ------------------------------------

    def click(self):

        element = SelfHealing.find_element(
            driver=self.driver,
            wait=self.wait,
            locator=self.locator,
            condition=EC.element_to_be_clickable
        )

        element.click()

    # ------------------------------------

    def send_keys(self, value):

        element = SelfHealing.find_element(
            driver=self.driver,
            wait=self.wait,
            locator=self.locator,
            condition=EC.visibility_of_element_located
        )

        element.clear()
        element.send_keys(value)

    # ------------------------------------

    def text(self):

        return self._find().text

    # ------------------------------------

    def get_attribute(self, name):

        return self._find().get_attribute(name)

    # ------------------------------------

    def is_displayed(self):

        return self._find().is_displayed()

    # ------------------------------------

    def raw(self):

        """
        Returns the underlying Selenium WebElement.
        """

        return self._find()