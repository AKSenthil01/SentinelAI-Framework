"""
Enterprise Strategy Recovery

Attempts deterministic locator recovery before AI.
"""

from selenium.webdriver.common.by import By

from utils.healing.healing_base import HealingBase
from utils.healing.console_logger import ConsoleLogger
from utils.healing_logger import HealingLogger
from utils.locator_repository import LocatorRepository


class StrategyRecovery(HealingBase):

    def recover(
            self,
            driver,
            wait,
            locator,
            condition
    ):

        ConsoleLogger.trying("Strategy")

        by, value = locator

        candidates = []

        #
        # ID recovery
        #

        if by == By.ID:

            candidates.extend([

                (By.CSS_SELECTOR, f"[id='{value}']"),

                (By.CSS_SELECTOR, f"#{value}")

            ])

        #
        # NAME recovery
        #

        elif by == By.NAME:

            candidates.extend([

                (By.CSS_SELECTOR, f"[name='{value}']"),

                (By.XPATH, f"//*[@name='{value}']")

            ])

        #
        # XPATH recovery
        #

        elif by == By.XPATH:

            #
            # Download Invoice
            #

            if "Download Invoice" in value:

                candidates.extend([

                    (By.CSS_SELECTOR, "[data-qa='download-invoice']"),

                    (By.LINK_TEXT, "Download Invoice"),

                    (By.PARTIAL_LINK_TEXT, "Invoice")

                ])

            #
            # Continue
            #

            elif "Continue" in value:

                candidates.extend([

                    (By.LINK_TEXT, "Continue"),

                    (By.PARTIAL_LINK_TEXT, "Continue"),

                    (By.XPATH, "//*[normalize-space()='Continue']")

                ])

            #
            # Home
            #

            elif "Home" in value:

                candidates.extend([

                    (By.CSS_SELECTOR, "[data-qa='home']"),

                    (By.LINK_TEXT, "Home"),

                    (By.XPATH, "//*[normalize-space()='Home']")

                ])

        #
        # Try every candidate
        #

        for recovered_locator in candidates:

            try:

                element = wait.until(

                    condition(recovered_locator)

                )

                #
                # Learn
                #

                LocatorRepository.add_locator(

                    locator[0],

                    locator[1],

                    recovered_locator,

                    source="Strategy"

                )

                LocatorRepository.record_success(

                    locator[0],

                    locator[1],

                    recovered_locator

                )

                HealingLogger.log(

                    original=locator,

                    recovered=recovered_locator,

                    source="Strategy",

                    provider="LocatorStrategy",

                    confidence=90,

                    reason="Deterministic recovery",

                    duration_ms=0,

                    repository_updated=True

                )

                ConsoleLogger.success(

                    engine="Strategy",

                    original=locator,

                    recovered=recovered_locator,

                    duration=0,

                    confidence=90,

                    provider="LocatorStrategy"

                )

                return element

            except Exception:

                continue

        ConsoleLogger.failed("Strategy")

        return None