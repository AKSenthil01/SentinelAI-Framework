import time

from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def scroll_to_and_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        #self.handle_google_vignette() #AD popup close


    def page_title(self):
        return self.driver.title

    def waitForElement(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def clickElement(self,locator):
        element=self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        #self.handle_google_vignette()  # AD popup close

    def validateElement(self,locator):
        return locator.is_displayed()

    def inputText(self,value,locator):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)
        #Previously working
        # element = self.driver.find_element(*locator)
        # element.clear()
        # element.send_keys(value)

    def validateMsg(self,locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except:
            return False

    def getElements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    # def handle_google_vignette(self):
    #     """
    #     Handles the full-screen Google Ad popup that appears on Automation Exercise.
    #     """
    #     try:
    #         # 1. Look for the ad iframe (usually starts with 'aswift_')
    #         # We wait a very short time (2s) so we don't slow down the test if there's no ad
    #         ad_iframe = self.driver.find_elements(By.ID, "aswift_1")
    #
    #         if len(ad_iframe) > 0:
    #             self.driver.switch_to.frame("aswift_1")
    #
    #             # Sometimes there is a second nested iframe
    #             nested_iframe = self.driver.find_elements(By.ID, "ad_iframe")
    #             if len(nested_iframe) > 0:
    #                 self.driver.switch_to.frame("ad_iframe")
    #
    #             # 2. Click the Dismiss/Close button
    #             # The ID is usually 'dismiss-button'
    #             dismiss_btn = self.driver.find_elements(By.ID, "dismiss-button")
    #             if len(dismiss_btn) > 0:
    #                 dismiss_btn[0].click()
    #
    #             # 3. Always switch back to the main page
    #             self.driver.switch_to.default_content()
    #             print("AD handled successfully.")
    #     except Exception as e:
    #         self.driver.switch_to.default_content()
    #         print(f"No ad appeared or error handling ad: {e}")
    #
    # def close_ad_if_present(self):
    #     """
    #     A robust 'look-through' for the Google Vignette Dismiss button.
    #     """
    #     try:
    #         # Google Ads often use this specific ID for the container
    #         if self.driver.find_elements(By.ID, "aswift_1"):
    #             self.driver.switch_to.frame("aswift_1")
    #             if self.driver.find_elements(By.ID, "ad_iframe"):
    #                 self.driver.switch_to.frame("ad_iframe")
    #
    #             # Use JS to click the dismiss button as it's often 'unclickable' by standard Selenium
    #             self.driver.execute_script("document.getElementById('dismiss-button').click();")
    #             self.driver.switch_to.default_content()
    #     except:
    #         self.driver.switch_to.default_content()

    # def click_button_safely(self, locator):
    #     """
    #     A senior-level clicker that handles Google Vignette ads
    #     by forcing a JavaScript click if the UI is blocked.
    #     """
    #     try:
    #         # 1. Wait for element to be present
    #         element = self.wait.until(EC.presence_of_element_to_be_clickable(locator))
    #
    #         # 2. Try standard Selenium click
    #         element.click()
    #
    #     except ElementClickInterceptedException:
    #         # 3. If blocked by an ad, use JavaScript to click 'underneath' the ad
    #         print("Click intercepted by Ad. Using JavaScript bypass...")
    #         self.driver.execute_script("arguments[0].click();", element)
    #
    #     # 4. Handle the URL if it gets stuck on '#google_vignette'
    #     if "#google_vignette" in self.driver.current_url:
    #         clean_url = self.driver.current_url.split("#")[0]
    #         self.driver.execute_script(f"window.location.href='{clean_url}'")

    #

    def click_element(self, locator):
        """Custom clicker that cleans ads first."""
        #self.remove_ads_from_dom()  # Clean before click
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        #self.remove_ads_from_dom()  # Clean after click (for next step)

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