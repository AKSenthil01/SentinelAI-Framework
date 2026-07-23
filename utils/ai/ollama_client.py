"""
Enterprise Ollama Client

Responsible for communicating with the local Ollama server.

Features
--------
✔ Retry
✔ Timeout
✔ Error handling
✔ JSON response
✔ Easy to extend
"""

from __future__ import annotations

import json
import requests

from utils.ai_config import (
    OLLAMA_MODEL,
    OLLAMA_URL
)


class OllamaClient:

    TIMEOUT = 180

    RETRIES = 2

    @staticmethod
    def generate(prompt: str) -> dict:
        """
        Sends prompt to Ollama.

        Returns

        {
            success: bool,
            response: str,
            error: str
        }
        """
        print(f"\nOLLAMA URL   : {OLLAMA_URL}")
        print(f"OLLAMA MODEL : {OLLAMA_MODEL}")

        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }

        last_error = None

        for attempt in range(OllamaClient.RETRIES):

            try:

                print("\nSending prompt to Ollama...")
                print("\n================ PROMPT SIZE =================")
                print("Characters :", len(prompt))
                print("==============================================\n")

                response = requests.post(
                    OLLAMA_URL,
                    json=payload,
                    timeout=OllamaClient.TIMEOUT
                )

                response.raise_for_status()

                print("HTTP Status :", response.status_code)

                #
                print("\n================ RAW HTTP RESPONSE ================")
                print(response.text)
                print("===================================================\n")

                data = response.json()

                print("\n================ PARSED JSON =======================")
                print(data)
                print("===================================================\n")

                print("\n================ AI RESPONSE FIELD =================")
                print(repr(data.get("response")))
                print("===================================================\n")

                return {
                    "success": True,
                    "response": data.get("response", ""),
                    "error": None
                }


            except Exception as ex:

                print("\nOLLAMA ERROR")

                print(ex)

                last_error = str(ex)

                last_error = str(ex)

        return {
            "success": False,
            "response": "",
            "error": last_error
        }

    @staticmethod
    def generate_json(prompt: str) -> dict:
        """
        Asks Ollama and expects JSON.

        If parsing fails,
        raw response is returned.
        """

        result = OllamaClient.generate(prompt)


        if not result["success"]:

            return result

        text = result["response"].strip()

        #
        # Remove markdown if Llama returns
        # ```json
        # ...
        # ```
        #

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        try:

            parsed = json.loads(text)

            return {
                "success": True,
                "response": parsed,
                "error": None
            }

        except Exception:

            return {
                "success": False,
                "response": text,
                "error": "Invalid JSON returned by Llama"
            }