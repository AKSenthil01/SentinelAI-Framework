import os
from dotenv import load_dotenv

load_dotenv()

AI_ENABLED = os.getenv(
    "AI_ENABLED",
    "True"
).lower() == "true"

AI_PROVIDER = os.getenv(
    "AI_PROVIDER",
    "llama"
).lower()

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3:8b"
)