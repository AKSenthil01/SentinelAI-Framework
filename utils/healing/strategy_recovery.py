"""
Strategy Recovery Engine

Generates alternative locators using predefined
heuristics and naming strategies.
"""

import time

from selenium.common.exceptions import TimeoutException

from utils.healing.healing_base import HealingBase
from utils.healing.console_logger import ConsoleLogger
from utils.healing_logger import HealingLogger
from utils.locator_repository import LocatorRepository
from utils.locator_strategy import LocatorStrategy


class StrategyRecovery(HealingBase):

    def recover(

            self,

            driver,

            wait,

            locator,

            condition

    ):

        by, value = locator

        ConsoleLogger.trying("Strategy")

        candidates = LocatorStrategy.generate(

            by,

            value

        )

        if not candidates:

            ConsoleLogger.failed("Strategy")

            return None

        for candidate in candidates:

            start = time.perf_counter()

            try:

                element = wait.until(

                    condition(candidate)

                )

                duration = (

                    time.perf_counter() - start

                ) * 1000

                #
                # Learn this locator
                #

                LocatorRepository.add_locator(

                    by,

                    value,

                    candidate,

                    source="Strategy"

                )

                LocatorRepository.record_success(

                    by,

                    value,

                    candidate

                )

                #
                # Healing Log
                #

                HealingLogger.log(

                    original=locator,

                    recovered=candidate,

                    source="Strategy",

                    provider="LocatorStrategy",

                    confidence=90,

                    duration_ms=round(duration, 2),

                    repository_updated=True

                )

                #
                # Console Output
                #

                ConsoleLogger.success(

                    engine="Strategy",

                    original=locator,

                    recovered=candidate,

                    duration=duration,

                    confidence=90,

                    provider="LocatorStrategy"

                )

                ConsoleLogger.finished()

                return element

            except TimeoutException:

                LocatorRepository.record_failure(

                    by,

                    value,

                    candidate

                )

        ConsoleLogger.failed("Strategy")

        return None