from selenium.webdriver.common.by import By


class AIDemoPage:

    PLACE_ORDER = (
        By.ID,
        "submit"          # intentionally wrong
    )

    def __init__(self, driver):

        self.driver = driver

    def open(self, path):

        self.driver.get(path)

    def click_place_order(self):

        self.driver.find_element(
            *self.PLACE_ORDER
        ).click()