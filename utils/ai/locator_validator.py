
"""
Enterprise Locator Validator

Responsibilities
----------------
✔ Validate AI generated locator
✔ Reject hallucinated locators
✔ Reject invalid locator syntax
✔ Ensure locator exists on page
"""

from __future__ import annotations

from selenium.webdriver.common.by import By


class LocatorValidator:

    BY_MAPPING = {
        "id": By.ID,
        "name": By.NAME,
        "css selector": By.CSS_SELECTOR,
        "xpath": By.XPATH,
    }

    @staticmethod
    def validate(driver, locator):

        if locator is None:
            return None

        if len(locator) != 2:
            return None

        by, value = locator

        if by not in LocatorValidator.BY_MAPPING:
            return None

        selenium_by = LocatorValidator.BY_MAPPING[by]

        try:

            elements = driver.find_elements(
                selenium_by,
                value
            )

            if len(elements) == 0:

                print()

                print("======================================")
                print("AI locator rejected")
                print(locator)
                print("Reason : Element not found")
                print("======================================")

                return None

            print()

            print("======================================")
            print("Validated locator")
            print(locator)
            print("======================================")

            return locator

        except Exception:

            return None
