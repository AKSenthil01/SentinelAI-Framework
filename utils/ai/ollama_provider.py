"""
Enterprise Ollama Provider

Responsibilities
----------------
✔ Extract DOM
✔ Build Prompt
✔ Query Ollama
✔ Parse response
✔ Validate locator
✔ Validate semantic similarity
✔ Update repository
✔ Return standardized recovery result
"""

from __future__ import annotations
from utils.ai.ai_session import AISession
import re
import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.ai.dom_extractor import DOMExtractor
from utils.ai.prompt_builder import PromptBuilder
from utils.ai.ollama_client import OllamaClient

from utils.healing.repository_updater import RepositoryUpdater
from utils.healing.recovery_validator import RecoveryValidator


class OllamaProvider:

    PROVIDER_NAME = "Ollama"

    # -----------------------------------------------------

    def suggest_locators(
            self,
            failed_locator,
            driver
    ):

        try:

            page_title = driver.title
            page_url = driver.current_url

            html = DOMExtractor.extract(
                driver,
                failed_locator
            )

            from utils.ai.candidate_ranker import CandidateRanker

            html = CandidateRanker.rank(
                html,
                failed_locator
            )

            # print("=" * 80)
            # print("DOM SENT TO OLLAMA")
            # print("=" * 80)
            # print(html)
            # print("=" * 80)

            print("\n")
            print("=" * 100)
            print("TOP CANDIDATE DOM SENT TO OLLAMA")
            print("=" * 100)
            print(html)
            print("=" * 100)

            prompt = PromptBuilder.build_locator_prompt(
                locator=failed_locator,
                page_title=page_title,
                page_url=page_url,
                html=html
            )

            print("\n" + "=" * 80)
            print("PROMPT SENT TO OLLAMA")
            print("=" * 80)
            print(prompt)
            print("=" * 80)

            print("\n==============================")
            print("Sending Prompt To Ollama")
            print("==============================")

            result = OllamaClient.generate(prompt)

            print("\n" + "=" * 80)
            print("RAW OLLAMA RESULT")
            print("=" * 80)
            print(result)
            print("=" * 80)

            print("\n==============================")
            print("OLLAMA RESPONSE")
            print("==============================")
            print(result.get("response"))
            print("==============================\n")

            AISession.save(
                prompt,
                result.get("response", "")
            )

            if not result["success"]:
                return None

            raw_text = result["response"]

            locator = self._parse_locator(raw_text)

            #
            # AI returned nothing?
            #

            if locator is None:
                return None

            #
            # AI locator valid?
            #

            if self._validate_locator(locator, driver):
                return {

                    "provider": self.PROVIDER_NAME,

                    "confidence": 95,

                    "reason": "Recovered using Ollama",

                    "locators": [locator]

                }

            #
            # AI locator invalid.
            # Try visible text.
            #

            button_text = self._extract_button_text(html)

            locator = self._find_by_text(

                driver,

                button_text

            )

            if locator:
                return {

                    "provider": self.PROVIDER_NAME,

                    "confidence": 90,

                    "reason": "Recovered using visible text",

                    "locators": [locator]

                }

            ###return None
            #
            # Validate recovered locator exists
            #

            if not self._validate_locator(
                        locator,
                        driver
                ):
                print("\nLocator validation failed.")
                return None

            #
            # Semantic validation
            #

            if not RecoveryValidator.validate(
                        driver,
                        failed_locator,
                        locator
                ):
                print("\nRecovery rejected by semantic validator.")
                return None

            #
            # Learn successful recovery
            #
            #
            # RepositoryUpdater.update(
            #         failed_locator,
            #         locator
            #     )
            # if locator[0] in (
            #
            #         By.ID,
            #
            #         By.NAME
            #
            # ):
            #     RepositoryUpdater.update(
            #         failed_locator,
            #         locator
            #     )
            # print("\nRepository updated successfully.")

            #
            # Standard response
            #

            return {

                    "provider": self.PROVIDER_NAME,

                    "confidence": 95,

                    "reason": "Recovered using Ollama",

                    "locators": [locator]

                }

        except Exception:

            print("\n========== OLLAMA PROVIDER ERROR ==========\n")

            traceback.print_exc()

            print("\n===========================================\n")

            return None

        # -----------------------------------------------------

    # def _validate_locator(
    #         self,
    #         locator,
    #         driver
    # ):
    #
    #     try:
    #
    #         by, value = locator
    #
    #         WebDriverWait(
    #             driver,
    #             10
    #         ).until(
    #
    #             EC.presence_of_element_located(
    #
    #                 (by, value)
    #
    #             )
    #
    #         )
    #
    #         return True
    #
    #     except TimeoutException:
    #
    #         print("\nLocator not found within timeout.")
    #
    #         return False
    #
    #     except Exception as ex:
    #
    #         print("\nLocator validation exception:")
    #
    #         print(type(ex).__name__)
    #
    #         print(ex)
    #
    #         return False
    def _validate_locator(self, locator, driver):

        try:

            by, value = locator

            element = driver.find_element(by, value)

            tag = element.tag_name.lower()

            #
            # Reject icons
            #

            if tag in ("i", "svg"):
                print("Rejected icon locator")

                return False

            return True

        except Exception:

            return False

    #
    #     # -----------------------------------------------------

    # def _parse_locator(
    #         self,
    #         text
    # ):
    #
    #     """
    #     Parses Ollama output into a Selenium locator.
    #
    #     Supports outputs like:
    #
    #         id=submit
    #         css=#submit
    #         xpath=//button[@id='submit']
    #         name=pay-button
    #
    #     AI explanations are ignored.
    #     """
    #     if "NOT_FOUND" in text.upper():
    #         return None
    #
    #     if not text:
    #         return None
    #
    #     #
    #     # Remove markdown fences
    #     #
    #
    #     text = (
    #         text.replace("```", "")
    #             .replace("`", "")
    #             .strip()
    #     )
    #
    #     #
    #     # Find every locator-looking line.
    #     # AI usually gives the correct locator first.
    #     #
    #
    #     # matches = re.findall(
    #     #     r"(id|name|css|xpath)\s*=\s*([^\n\r]+)",
    #     #     text,
    #     #     flags=re.IGNORECASE
    #     # )
    #
    #     matches = re.findall(
    #         r"(id|name|css selecto|xpath|data-qa|data-testid|aria-label)\s*=\s*[\"']?([^\n\r\"']+)",
    #         text,
    #         flags=re.IGNORECASE
    #     )
    #
    #     if matches:
    #
    #         #
    #         # Prefer FIRST valid locator
    #         #
    #
    #         by, value = matches[0]
    #
    #         value = value.strip()
    #
    #         #
    #         # Remove quotes
    #         #
    #
    #         value = value.strip('"').strip("'")
    #
    #         #
    #         # Remove trailing punctuation
    #         #
    #
    #         value = value.rstrip(".,;:")
    #         key = by.lower()
    #
    #         if key == "data-qa":
    #             value = f'[data-qa="{value}"]'
    #
    #         elif key == "data-testid":
    #             value = f'[data-testid="{value}"]'
    #
    #         elif key == "aria-label":
    #             value = f'[aria-label="{value}"]'
    #         #
    #         # mapping = {
    #         #
    #         #     "id": By.ID,
    #         #
    #         #     "name": By.NAME,
    #         #
    #         #     "css": By.CSS_SELECTOR,
    #         #
    #         #     "xpath": By.XPATH
    #         #
    #         #}
    #         mapping = {
    #
    #             "id": By.ID,
    #
    #             "name": By.NAME,
    #
    #             "css": By.CSS_SELECTOR,
    #
    #             "css selector": By.CSS_SELECTOR,
    #
    #             "xpath": By.XPATH
    #
    #         }
    #
    #         # locator = (
    #         #
    #         #     mapping[by.lower()],
    #         #
    #         #     value
    #         #
    #         # )
    #
    #         locator = (
    #             mapping[key],
    #             value
    #         )
    #
    #         print("\nRecovered locator:")
    #
    #         print(locator)
    #
    #         return locator
    #
    #     #
    #     # Bare XPath
    #     #
    #
    #     text = text.strip()
    #
    #     if text.startswith("//"):
    #
    #         return (
    #
    #             By.XPATH,
    #
    #             text
    #
    #         )
    #
    #     #
    #     # Bare CSS id
    #     #
    #
    #     if text.startswith("#"):
    #
    #         return (
    #
    #             By.CSS_SELECTOR,
    #
    #             text
    #
    #         )
    #
    #     #
    #     # Bare id only
    #     #
    #
    #     if re.fullmatch(
    #
    #             r"[A-Za-z_][A-Za-z0-9_\-]*",
    #
    #             text
    #
    #     ):
    #
    #         return (
    #
    #             By.ID,
    #
    #             text
    #
    #         )
    #
    #     print("\nUnable to parse locator from AI response.")
    #
    #     return None

    def _parse_locator(self, text):

        from selenium.webdriver.common.by import By
        import re

        if not text:
            return None

        text = (
            text.replace("```", "")
            .replace("`", "")
            .strip()
        )

        #
        # Extract ALL locator lines
        #

        patterns = [

            (By.ID,
             r"id\s*=\s*([^\n\r]+)"),

            (By.NAME,
             r"name\s*=\s*([^\n\r]+)"),

            (By.CSS_SELECTOR,
             r"css\s*=\s*([^\n\r]+)"),

            (By.XPATH,
             r"xpath\s*=\s*([^\n\r]+)"),

        ]

        candidates = []

        for by, pattern in patterns:

            matches = re.findall(
                pattern,
                text,
                flags=re.IGNORECASE
            )

            for m in matches:
                value = (
                    m.strip()
                    .strip("'")
                    .strip('"')
                    .rstrip(".,;:")
                )

                candidates.append((by, value))

        if not candidates:
            print("\nUnable to parse locator.")

            return None

        #
        # IMPORTANT
        #
        # AI repeats broken locator first.
        # Recovery locator comes LAST.
        #

        locator = candidates[-1]

        print("\nRecovered locator:")
        print(locator)

        return locator

    def _find_by_text(self, driver, text):

        if not text:
            return None

        xpath = f"//*[normalize-space(text())='{text}']"

        try:
            driver.find_element(By.XPATH, xpath)

            return (
                By.XPATH,
                xpath
            )

        except Exception:

            return None

    def _extract_button_text(self, html):

        import re

        m = re.search(

            r">(.*?)<",

            html,

            re.DOTALL

        )

        if not m:
            return None

        text = m.group(1)

        text = re.sub(r"\s+", " ", text)

        return text.strip()
