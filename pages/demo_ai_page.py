from selenium.webdriver.common.by import By


class DemoAIPage:

    # Intentionally wrong locator
    BTN_PLACE_ORDER = (
        By.ID,
        "submit123"
    )

    def __init__(self, driver):
        self.driver = driver

    def click_place_order(self):
        self.driver.find_element(
            *self.BTN_PLACE_ORDER
        ).click()