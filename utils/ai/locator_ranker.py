from selenium.webdriver.common.by import By


class LocatorRanker:

    SCORES = {
        By.ID: 100,
        By.NAME: 95,
        By.CSS_SELECTOR: 90,
        By.XPATH: 80,
        By.CLASS_NAME: 70
    }

    @staticmethod
    def rank(candidates):

        return sorted(
            candidates,
            key=lambda c: LocatorRanker.SCORES.get(c[0], 0),
            reverse=True
        )