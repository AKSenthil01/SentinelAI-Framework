from abc import ABC, abstractmethod


class BaseAIAdvisor(ABC):

    @abstractmethod
    def suggest_locator(
            self,
            original_locator,
            driver
    ):
        """
        Returns XPath or None
        """
        pass