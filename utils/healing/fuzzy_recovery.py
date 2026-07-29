"""
Fuzzy Recovery Engine

Uses fuzzy string matching to recover broken locators.
"""

import time
from difflib import SequenceMatcher

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from utils.healing.healing_base import HealingBase
from utils.healing.console_logger import ConsoleLogger
from utils.healing_logger import HealingLogger
from utils.locator_repository import LocatorRepository


class FuzzyRecovery(HealingBase):

    SIMILARITY_THRESHOLD = 0.75

    def recover(

            self,

            driver,

            wait,

            locator,

            condition

    ):

        by, value = locator

        ConsoleLogger.trying("Fuzzy")

        #
        # Collect all elements
        #

        elements = driver.find_elements(By.XPATH, "//*")

        best_ratio = 0.0
        best_locator = None

        for element in elements:

            #
            # Candidate attributes
            #

            candidates = [

                ("id", element.get_attribute("id")),

                ("name", element.get_attribute("name")),

                ("data-testid", element.get_attribute("data-testid")),

                ("data-qa", element.get_attribute("data-qa")),

                ("aria-label", element.get_attribute("aria-label")),

                ("text", element.text)

            ]

            for attr, candidate in candidates:

                if not candidate:

                    continue

                candidate = candidate.strip()

                if not candidate:
                    continue

                ratio = SequenceMatcher(

                    None,

                    value.lower(),

                    candidate.lower()

                ).ratio()

                if ratio > best_ratio:

                    best_ratio = ratio

                    best_locator = (attr, candidate)

        #
        # No Similar Locator
        #

        if (

                best_locator is None

                or best_ratio < self.SIMILARITY_THRESHOLD

        ):

            ConsoleLogger.failed("Fuzzy")

            return None

        #
        # Convert to Selenium locator
        #

        attr, candidate = best_locator

        if attr == "id":

            recovered = (

                By.ID,

                candidate

            )

        elif attr == "name":

            recovered = (

                By.NAME,

                candidate

            )


        elif attr == "text":

            recovered = (

                By.XPATH,

                f"//*[normalize-space()='{candidate.strip()}']"

            )


        else:

            recovered = (

                By.XPATH,

                f"//*[@{attr}='{candidate}']"

            )

        start = time.perf_counter()

        try:

            element = wait.until(

                condition(recovered)

            )

            duration = (

                time.perf_counter() - start

            ) * 1000

            #
            # Learn
            #

            LocatorRepository.add_locator(

                by,

                value,

                recovered,

                source="Fuzzy"

            )

            LocatorRepository.record_success(

                by,

                value,

                recovered

            )

            #
            # Log
            #

            HealingLogger.log(

                original=locator,

                recovered=recovered,

                source="Fuzzy",

                provider="SequenceMatcher",

                confidence=round(best_ratio * 100),

                duration_ms=round(duration, 2),

                repository_updated=True

            )

            #
            # Console
            #

            ConsoleLogger.success(

                engine="Fuzzy",

                original=locator,

                recovered=recovered,

                duration=duration,

                confidence=round(best_ratio * 100),

                provider="SequenceMatcher"

            )

            ConsoleLogger.finished()

            return element

        except TimeoutException:

            LocatorRepository.record_failure(

                by,

                value,

                recovered

            )

            ConsoleLogger.failed("Fuzzy")

            return None