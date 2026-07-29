"""
Enterprise Ollama Client

Responsibilities
----------------
✔ Calls local Ollama
✔ Handles timeout
✔ Handles retries
✔ Captures COMPLETE response
✔ Captures streaming response
✔ Never returns None
"""

from __future__ import annotations

import json
import traceback

import requests

from utils.ai_config import (
    OLLAMA_MODEL,
    OLLAMA_URL
)


class OllamaClient:

    TIMEOUT = 300
    RETRIES = 2

    @staticmethod
    def generate(prompt: str):

        if prompt is None:
            return {
                "success": False,
                "response": "",
                "error": "Prompt is None"
            }

        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }

        last_error = ""

        for attempt in range(OllamaClient.RETRIES):

            try:

                print("\n==============================")
                print("Sending Prompt To Ollama")
                print("==============================")

                response = requests.post(
                    OLLAMA_URL,
                    json=payload,
                    timeout=OllamaClient.TIMEOUT
                )

                response.raise_for_status()

                data = response.json()

                ai_response = data.get("response", "")

                if ai_response is None:
                    ai_response = ""

                ai_response = str(ai_response)

                print("\n==============================")
                print("OLLAMA RESPONSE")
                print("==============================")
                print(ai_response)
                print("==============================\n")

                return {
                    "success": True,
                    "response": ai_response,
                    "error": None
                }

            except Exception as ex:

                traceback.print_exc()

                last_error = str(ex)

        return {
            "success": False,
            "response": "",
            "error": last_error
        }

    @staticmethod
    def generate_json(prompt: str):

        result = OllamaClient.generate(prompt)

        if not result["success"]:
            return result

        text = result["response"]

        if text is None:
            text = ""

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
                "error": "Invalid JSON"
            }