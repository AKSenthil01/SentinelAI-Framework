"""
Enterprise Ollama Provider

Responsibilities
----------------
✔ Extract DOM
✔ Build AI prompt
✔ Call Ollama
✔ Normalize response
✔ Validate locator
✔ Return structured recovery result
"""

from __future__ import annotations
from utils.ai.ai_logger import AILogger
import re
import traceback

from selenium.webdriver.common.by import By
from utils.ai.dom_extractor import DOMExtractor
from utils.ai.ollama_client import OllamaClient
from utils.ai.prompt_builder import PromptBuilder


class OllamaProvider:

    PROVIDER_NAME = "Ollama"

    # ---------------------------------------------

    def suggest_locators(self, failed_locator, driver):
        print("STEP-1")

        try:
            print("STEP-2")

            page_title = driver.title
            page_url = driver.current_url
            print("STEP-3")

            html = DOMExtractor.extract(
                driver,
                failed_locator
            )
            print("STEP-4")

            prompt = PromptBuilder.build_locator_prompt(
                locator=failed_locator,
                page_title=page_title,
                page_url=page_url,
                html=html
            )

            print("PROMPT TYPE =", type(prompt))
            print("PROMPT IS NONE =", prompt is None)

            AILogger.write(
                "PROMPT",
                prompt
            )
            print("STEP-5")

            MAX_AI_ATTEMPTS = 3

            result = None

            for attempt in range(MAX_AI_ATTEMPTS):

                print(f"\nAI Attempt {attempt + 1}")

                result = OllamaClient.generate(prompt)

                if not result["success"]:
                    continue

                locator = self._parse_locator(result["response"])

                if locator is None:
                    continue

                from utils.ai.locator_validator import LocatorValidator

                if LocatorValidator.exists(driver, locator):
                    print("Validated locator:", locator)

                    return {
                        "provider": self.PROVIDER_NAME,
                        "confidence": 95,
                        "reason": "Recovered by Ollama",
                        "locators": [locator]
                    }

                print("AI returned invalid locator:", locator)

                prompt += """

            IMPORTANT

            The locator you suggested DOES NOT EXIST.

            Return ONLY a locator that already exists inside the supplied HTML.

            Never invent ids.

            """

            return None

            AILogger.write(
                "OLLAMA RAW RESPONSE",
                result
            )

            print("STEP-6")

            print("\n========== OLLAMA RAW RESPONSE ==========")
            print(result["response"])
            print("=========================================\n")

            if not result["success"]:

                return None

            print("\n========== OLLAMA RAW TEXT ==========")
            print(result["response"])
            print("=====================================\n")

            locator = self._parse_locator(
                result["response"]
            )

            from utils.ai.locator_validator import LocatorValidator

            if not LocatorValidator.exists(driver, locator):
                print("\nLLM returned INVALID locator.")

                print(locator)

                return None

            #
            # Validate against live DOM
            #

            try:
                driver.find_element(*locator)

                print("Locator validated")

                return {
                    ...
                }

            except Exception:

                print("LLM returned invalid locator")

                locator = None

            AILogger.write(
                "PARSED LOCATOR",
                locator
            )
            with open("ollama_response.txt", "w", encoding="utf-8") as f:
                f.write(result.get("response", ""))

            print("\n========== PARSED LOCATOR ==========")
            print(locator)
            print("====================================\n")

            if locator is None:

                return None

            # return {
            #
            #     "provider": self.PROVIDER_NAME,
            #
            #     "confidence": 95,
            #
            #     "reason": "Recovered by local Ollama",
            #
            #     "locators": [
            #
            #         locator
            #
            #     ]
            #
            # }
            return {
                "provider": self.PROVIDER_NAME,
                "confidence": 95,
                "reason": "Recovered by Ollama",
                "locator": locator
            }

            recovered_locator = result["locator"]


        except Exception:

            print("\n========== OLLAMA EXCEPTION ==========\n")

            tb = traceback.format_exc()

            AILogger.write(
                "EXCEPTION",
                tb
            )

            print(tb)

            print("\n======================================\n")

            return None

    # ---------------------------------------------

    from selenium.webdriver.common.by import By
    import re

    import re

    def _parse_locator(self, text):

        print(text)

        text = text.replace("```", "")
        text = text.replace("`", "")

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        mapping = {
            "id": By.ID,
            "name": By.NAME,
            "css": By.CSS_SELECTOR,
            "css selector": By.CSS_SELECTOR,
            "xpath": By.XPATH
        }

        for line in reversed(lines):

            m = re.match(
                r"^(id|name|css|css selector|xpath)\s*=\s*(.+)$",
                line,
                re.I
            )

            if not m:
                continue

            by = m.group(1).lower()
            value = m.group(2).strip()

            value = value.strip('"').strip("'")

            return (
                mapping[by],
                value
            )

        return None