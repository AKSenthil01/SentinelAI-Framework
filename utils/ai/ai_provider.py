from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    def suggest_locators(
        self,
        locator,
        driver
    ):
        pass


class MockAIProvider(AIProvider):

    def suggest_locators(
        self,
        locator,
        driver
    ):
        return None