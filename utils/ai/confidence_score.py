from selenium.webdriver.common.by import By


class ConfidenceScore:

    SCORE = {
        By.ID: 100,
        By.NAME: 95,
        By.CSS_SELECTOR: 90,
        By.XPATH: 80,
        By.CLASS_NAME: 70
    }

    @staticmethod
    def calculate(locator):

        return ConfidenceScore.SCORE.get(locator[0], 50)