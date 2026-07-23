from selenium.webdriver.common.by import By


class CandidateGenerator:
    """
    Generates intelligent locator candidates before AI is used.
    """

    @staticmethod
    def generate(locator):

        by, value = locator

        candidates = []

        # Original locator
        candidates.append(locator)

        if by == By.ID:

            candidates.extend([
                (By.CSS_SELECTOR, f"#{value}"),
                (By.XPATH, f"//*[@id='{value}']"),
                (By.NAME, value),
                (By.XPATH, f"//*[@name='{value}']"),
                (By.XPATH, f"//button[@id='{value}']"),
                (By.XPATH, f"//input[@id='{value}']")
            ])

        elif by == By.NAME:

            candidates.extend([
                (By.XPATH, f"//*[@name='{value}']"),
                (By.CSS_SELECTOR, f"[name='{value}']")
            ])

        elif by == By.CLASS_NAME:

            candidates.extend([
                (By.CSS_SELECTOR, f".{value}")
            ])

        # Remove duplicates
        unique = []

        for candidate in candidates:
            if candidate not in unique:
                unique.append(candidate)

        return unique