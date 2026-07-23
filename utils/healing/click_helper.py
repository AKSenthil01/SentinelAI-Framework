from selenium.common.exceptions import (
    ElementClickInterceptedException,
    WebDriverException
)


class ClickHelper:

    @staticmethod
    def click(driver, element):

        try:
            element.click()
            return

        except ElementClickInterceptedException:

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                element
            )

            try:
                element.click()
                return

            except Exception:
                pass

            driver.execute_script(
                "arguments[0].click();",
                element
            )

        except WebDriverException:

            driver.execute_script(
                "arguments[0].click();",
                element
            )