"""
Base class for all Healing Engines.

Every recovery engine must inherit from this class.
"""

from abc import ABC, abstractmethod


class HealingBase(ABC):

    @abstractmethod
    def recover(
        self,
        driver,
        wait,
        locator,
        condition
    ):
        """
        Try recovering a broken locator.

        Returns
        -------
        Selenium WebElement
            if recovery succeeds

        None
            if recovery fails
        """
        pass