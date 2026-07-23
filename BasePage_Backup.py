import time

from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.self_healing import SelfHealing


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # def scroll_to_and_click(self, locator):
    #     element = self.wait.until(EC.presence_of_element_located(locator))
    #
    #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    #     self.wait.until(EC.element_to_be_clickable(locator)).click()
    #     #self.handle_google_vignette() #AD popup close

    def scroll_to_and_click(self, locator):

        element = self.getElement(

            locator,

            EC.element_to_be_clickable

        )

        self.driver.execute_script(

            "arguments[0].scrollIntoView({block:'center'});",

            element

        )

        element.click()

    def clearText(self, locator):

        self.getElement(

            locator,

            EC.visibility_of_element_located

        ).clear()

    def getAttribute(

            self,

            locator,

            attribute

    ):

        return self.getElement(

            locator,

            EC.visibility_of_element_located

        ).get_attribute(attribute)

    from selenium.webdriver.support.ui import Select

    def selectDropdown(

            self,

            locator,

            text

    ):

        Select(

            self.getElement(

                locator,

                EC.visibility_of_element_located

            )

        ).select_by_visible_text(text)

    def getElements(self, locator):

        return SelfHealing.find_all(

            self.driver,

            self.wait,

            locator

        )


    def page_title(self):
        return self.driver.title

    def waitForElement(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    # def clickElement(self,locator):
    #     element=self.wait.until(EC.element_to_be_clickable(locator))
    #     element.click()
    #     #self.handle_google_vignette()  # AD popup close

    from selenium.webdriver.support import expected_conditions as EC

    from utils.self_healing import SelfHealing

    def clickElement(self, locator):

        element = self.getElement(

            locator,

            EC.element_to_be_clickable

        )

        element.click()

    def validateElement(self,locator):
        return locator.is_displayed()

    # def inputText(self, locator, value):
    #
    #     element = SelfHealing.find(
    #
    #         self.driver,
    #
    #         self.wait,
    #
    #         locator,
    #
    #         EC.visibility_of_element_located
    #
    #     )
    #
    #     element.clear()
    #
    #     element.send_keys(value)

    # def validateMsg(self,locator):
    #     try:
    #         return self.driver.find_element(*locator).is_displayed()
    #     except:
    #         return False

    # def getElements(self, locator):
    #     return self.wait.until(EC.presence_of_all_elements_located(locator))

    from selenium.webdriver.support import expected_conditions as EC
    from utils.self_healing import SelfHealing

    def getElement(

            self,

            locator,

            condition=EC.presence_of_element_located

    ):

        return SelfHealing.find(

            self.driver,

            self.wait,

            locator,

            condition

        )


    # def click_element(self, locator):
    #     """Custom clicker that cleans ads first."""
    #     #self.remove_ads_from_dom()  # Clean before click
    #     element = self.wait.until(EC.element_to_be_clickable(locator))
    #     element.click()
    #     #self.remove_ads_from_dom()  # Clean after click (for next step)

    # def getText(self, locator):
    #
    #     element = SelfHealing.find(
    #
    #         self.driver,
    #
    #         self.wait,
    #
    #         locator,
    #
    #         EC.visibility_of_element_located
    #
    #     )
    #
    #     return element.text

    def isDisplayed(self, locator):

        return self.getElement(

            locator,

            EC.visibility_of_element_located

        ).is_displayed()

    def validateMsg(self, locator):

        try:

            return self.isDisplayed(locator)

        except Exception:

            return False

    def getElement(self, locator):

        return SelfHealing.find(

            self.driver,

            self.wait,

            locator,

            EC.presence_of_element_located

        )

    def inputText(self, locator, value):

        element = self.getElement(

            locator,

            EC.visibility_of_element_located

        )

        element.clear()

        element.send_keys(value)

    def getText(self, locator):

        return self.getElement(

            locator,

            EC.visibility_of_element_located

        ).text

    def getElements(self, locator):

        return self.wait.until(

            EC.presence_of_all_elements_located(locator)

        )

    # def remove_ads_from_dom(self):
    #     """Removes Google Ad elements that block clicks."""
    #     script = """
    #     var ads = document.querySelectorAll('ins.adsbygoogle, div[id*="google_ads"], iframe[id*="aswift"], iframe[id*="ad_iframe"]');
    #     for (var i = 0; i < ads.length; i++) {
    #         ads[i].remove();
    #     }
    #     document.body.style.overflow = 'auto';
    #     """
    #     self.driver.execute_script(script)

    # def wait_for_page_ready(self, timeout=10):
    #     """
    #     Ensures the document is loaded and no ad-overlay is active.
    #     """
    #     # 1. Wait for JS to report 'complete'
    #     self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    #
    #     # 2. Check if we are stuck on an ad URL and force-clear it
    #     start_time = time.time()
    #     while "#google_vignette" in self.driver.current_url and (time.time() - start_time) < timeout:
    #         clean_url = self.driver.current_url.split("#")[0]
    #         self.driver.get(clean_url)
    #         self.remove_ads_from_dom()
    #         time.sleep(0.5)  # Short pulse to allow redirect

    # def click_and_bypass(self, locator):
    #     """
    #     Clicks and immediately checks if we are trapped in an ad URL.
    #     """
    #     self.driver.find_element(*locator).click()
    #
    #     # Wait a split second for the ad to trigger
    #     import time
    #     time.sleep(1)
    #
    #     # If the URL is trapped, strip the ad part and force-navigate
    #     if "#google_vignette" in self.driver.current_url:
    #         clean_url = self.driver.current_url.split("#")[0]
    #         #self.driver.get(clean_url)
    #         self.driver.get(clean_url)
    #         print(f"Ad Bypassed. Navigated to: {clean_url}")

    def click_and_bypass_fast(self, locator):
        """
        Optimized for speed: Clicks and immediately forces navigation
        if an ad is detected, without waiting for the ad to load.
        """
        # 1. Set a very short page load timeout just for this click
        # This prevents the 2-minute 'hanging' state
        self.driver.set_page_load_timeout(5)

        try:
            element = self.driver.find_element(*locator)
            element.click()
        except TimeoutException:
            # If the page 'hangs' because of an ad, this catch triggers immediately
            pass
        except Exception:
            # Fallback to JS click if blocked
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*locator))

        # 2. Immediate URL Check (Heartbeat)
        # We check the URL every 500ms for a maximum of 3 seconds
        for _ in range(6):
            current_url = self.driver.current_url
            if "#google_vignette" in current_url:
                clean_url = current_url.split("#")[0]
                print(f"Ad detected. Executing Fast-Bypass to: {clean_url}")
                self.driver.get(clean_url)
                break
            time.sleep(0.5)

        # 3. Reset timeout to standard (e.g., 30s) for the rest of the test
        self.driver.set_page_load_timeout(30)

    def cleanUrl(self):
        time.sleep(1)
        if "#google_vignette" in self.driver.current_url:
            clean_url = self.driver.current_url.split("#")[0]
            #self.driver.get(clean_url)
            self.driver.get(clean_url)
            print(f"Ad Bypassed. Navigated to: {clean_url}")

    def click_and_bypass(self, locator, destination_url_part):
        """
        The most aggressive bypass:
        1. Clicks via JS (non-blocking).
        2. Force-redirects if an ad is detected within 2 seconds.
        """
        self.driver.set_page_load_timeout(10)
        element = self.driver.find_element(*locator)

        # 1. Trigger the click via JS so Selenium doesn't 'wait' for the next page
        self.driver.execute_script("arguments[0].click();", element)

        # 2. Fast-polling (check every 200ms)
        for _ in range(15):
            current_url = self.driver.current_url

            # If we hit the Ad URL
            if "#google_vignette" in current_url:
                print("Ad detected! Killing it instantly.")
                clean_url = current_url.split("#")[0]
                self.driver.execute_script(f"window.location.href='{clean_url}'")
                return  # Exit once handled

            # If we already reached a 'clean' next page, stop waiting
            if destination_url_part in current_url and "#" not in current_url:
                return

            time.sleep(0.3)