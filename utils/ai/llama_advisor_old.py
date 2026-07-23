"""
Llama Advisor

Uses the local Ollama Llama model to suggest
robust Selenium locators.
"""

from selenium.webdriver.common.by import By

from utils.ai.prompt_builder import PromptBuilder
from utils.ai.ollama_client import OllamaClient
from utils.ai.dom_extractor import DOMExtractor


class LlamaAdvisor:

    def suggest_locators(self, locator, driver):
        """
        Returns

        {
            "reason": "...",
            "confidence": 96,
            "locators": [
                (By.XPATH, "..."),
                ...
            ]
        }

        Returns None if AI fails.
        """

        page_title = driver.title
        page_url = driver.current_url

        html = DOMExtractor.extract(
            driver,
            locator
        )

        prompt = PromptBuilder.build_locator_prompt(
            locator,
            page_title,
            page_url,
            html
        )

        result = OllamaClient.generate_json(prompt)

        if not result["success"]:

            print("\n========== AI FAILED ==========")
            print(result["error"])

            return None

        data = result["response"]

        try:

            confidence = data.get(
                "confidence",
                0
            )

            reason = data.get(
                "reason",
                ""
            )

            locators = []

            for xpath in data.get("locators", []):

                xpath = xpath.strip()

                if xpath:

                    locators.append(
                        (
                            By.XPATH,
                            xpath
                        )
                    )

            if not locators:

                return None

            print("\n========== LLAMA ==========")
            print("Reason      :", reason)
            print("Confidence  :", confidence)

            print("\nCandidates")

            for i, locator in enumerate(locators, start=1):

                print(f"{i}. {locator[1]}")

            return {

                "reason": reason,

                "confidence": confidence,

                "locators": locators

            }

        except Exception as ex:

            print("\nInvalid AI Response")

            print(ex)

            return None