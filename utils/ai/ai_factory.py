from utils.ai.ai_provider import MockAIProvider
from utils.ai.ollama_provider import OllamaProvider

from utils.ai_config import (
    AI_ENABLED,
    AI_PROVIDER
)


class AIAdvisorFactory:

    @staticmethod
    def get_advisor():

        if not AI_ENABLED:
            return MockAIProvider()

        provider = AI_PROVIDER.lower().strip()

        if provider in ("ollama", "llama"):
            return OllamaProvider()

        print(f"\nUnknown AI provider: {provider}")
        return MockAIProvider()