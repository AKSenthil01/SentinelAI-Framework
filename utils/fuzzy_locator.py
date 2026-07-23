from rapidfuzz import process
from selenium.webdriver.common.by import By


class FuzzyLocator:

    SCORE_THRESHOLD = 75

    @staticmethod
    def recover(driver, locator):

        by, value = locator

        if by != By.ID:
            return None

        ids = []

        elements = driver.find_elements(By.XPATH, "//*[@id]")

        for e in elements:

            try:
                ids.append(e.get_attribute("id"))
            except Exception:
                pass

        if not ids:
            return None

        match = process.extractOne(value, ids)

        if not match:
            return None

        best_id = match[0]
        score = match[1]

        print(f"\n[FUZZY] Best Match : {best_id}")
        print(f"[FUZZY] Similarity : {score}")

        if score < FuzzyLocator.SCORE_THRESHOLD:
            return None

        return (By.ID, best_id)