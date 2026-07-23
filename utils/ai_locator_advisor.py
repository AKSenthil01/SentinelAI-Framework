import requests

from utils.ai.ai_response_validator import AIResponseValidator
from utils.ai.dom_extractor import DOMExtractor
from utils.ai.prompt_builder import PromptBuilder


class AILocatorAdvisor:

    OLLAMA_URL = "http://localhost:11434/api/generate"

    MODEL = "llama3:8b"

    def suggest_locator(
            self,
            original_locator,
            driver
    ):

        html = DOMExtractor.extract(
            driver,
            original_locator
        )

        prompt = PromptBuilder.build_locator_prompt(
            original_locator,
            driver.title,
            driver.current_url,
            html
        )

        payload = {
            "model": self.MODEL,
            "prompt": prompt,
            "stream": False
        }

        try:

            response = requests.post(
                self.OLLAMA_URL,
                json=payload,
                timeout=90
            )

            response.raise_for_status()

            data = response.json()

            xpath = self.clean_response(
                data["response"]
            )

            if AIResponseValidator.is_valid_xpath(xpath):
                return xpath

        except Exception as ex:

            print(f"\nOllama Error : {ex}")

        return None

    @staticmethod
    def clean_response(text):

        text = text.strip()

        text = text.replace("```xpath", "")
        text = text.replace("```", "")

        text = text.replace('"', "")
        text = text.replace("'", "")

        if "//" in text:
            text = text[text.index("//"):]

        return text.strip()