from selenium.webdriver.common.by import By


class LocatorStrategy:
    """
    Generates intelligent fallback locator strategies
    from the original locator.
    """

    @staticmethod
    def generate(by, value):

        strategies = []

        by = str(by).lower()

        #
        # ID
        #
        if "id" in by:

            strategies.extend([

                (By.NAME, value),

                (By.CSS_SELECTOR, f"[id='{value}']"),

                (By.CSS_SELECTOR, f"[name='{value}']"),

                (By.XPATH, f"//*[@id='{value}']"),

                (By.XPATH, f"//*[@name='{value}']")

            ])

        #
        # NAME
        #
        elif "name" in by:

            strategies.extend([

                (By.ID, value),

                (By.CSS_SELECTOR, f"[name='{value}']"),

                (By.XPATH, f"//*[@name='{value}']")

            ])

        #
        # LINK TEXT
        #
        elif "link" in by:

            strategies.extend([

                (By.PARTIAL_LINK_TEXT, value),

                (By.XPATH, f"//*[contains(text(),'{value}')]")

            ])

        #
        # XPATH
        #
        elif "xpath" in by:

            strategies.append(

                (By.XPATH, value)

            )

        #
        # CSS
        #
        elif "css" in by:

            strategies.append(

                (By.CSS_SELECTOR, value)

            )

        return strategies