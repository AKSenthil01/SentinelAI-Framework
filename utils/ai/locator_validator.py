from selenium.webdriver.common.by import By


class LocatorValidator:

    MAP = {
        "id": By.ID,
        "name": By.NAME,
        "css selector": By.CSS_SELECTOR,
        "xpath": By.XPATH
    }

    @staticmethod
    def exists(driver, locator):

        if locator is None:
            return False

        by, value = locator

        selenium_by = LocatorValidator.MAP.get(by)

        if selenium_by is None:
            return False

        try:
            return len(driver.find_elements(selenium_by, value)) > 0

        except Exception:
            return False