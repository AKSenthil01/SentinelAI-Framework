from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    JavascriptException
)

from selenium.webdriver.common.action_chains import ActionChains


class ClickHelper:

    @staticmethod
    def click(driver, element):

        #
        # Try normal click
        #

        try:
            element.click()
            return

        except Exception:
            pass

        #
        # Scroll into view
        #

        try:

            driver.execute_script("""
                arguments[0].scrollIntoView({
                    behavior:'instant',
                    block:'center',
                    inline:'center'
                });
            """, element)

            element.click()
            return

        except Exception:
            pass

        #
        # Hide advertisements
        #

        try:

            driver.execute_script("""

                document.querySelectorAll(

                    "iframe[id^='aswift']," +

                    "iframe[title='Advertisement']," +

                    "iframe[src*='doubleclick']," +

                    "iframe[src*='googlesyndication']"

                ).forEach(function(frame){

                    frame.style.display='none';

                });

            """)

            element.click()
            return

        except Exception:
            pass

        #
        # ActionChains click
        #

        try:

            ActionChains(driver).move_to_element(element).click().perform()

            return

        except Exception:
            pass

        #
        # JavaScript click
        #

        try:

            driver.execute_script(
                "arguments[0].click();",
                element
            )

            return

        except JavascriptException:
            pass

        #
        # Last fallback
        #

        raise ElementClickInterceptedException(
            "Unable to click element even after all recovery strategies."
        )