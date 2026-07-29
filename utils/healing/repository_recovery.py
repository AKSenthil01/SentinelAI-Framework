"""
Repository Recovery Engine

This engine checks whether the broken locator
has already been healed in previous executions.
"""

import time




from utils.healing.healing_base import HealingBase
from utils.healing.console_logger import ConsoleLogger
from utils.healing_logger import HealingLogger
from utils.locator_repository import LocatorRepository
from selenium.common.exceptions import TimeoutException


class RepositoryRecovery(HealingBase):

    def recover(

            self,

            driver,

            wait,

            locator,

            condition

    ):

        by, value = locator

        ConsoleLogger.trying("Repository")

        alternatives = LocatorRepository.get_alternatives(

            by,

            value

        )

        if not alternatives:

            ConsoleLogger.failed("Repository")

            return None

        for alt in alternatives:

            start = time.perf_counter()

            try:

                element = wait.until(

                    condition(alt)

                )

                duration = (

                        time.perf_counter() - start

                ) * 1000

                #
                # Update Repository Statistics
                #

                LocatorRepository.record_success(

                    by,

                    value,

                    alt

                )

                #
                # Log Healing
                #

                HealingLogger.log(

                    original=locator,

                    recovered=alt,

                    source="Repository",

                    provider="Repository",

                    confidence=100,

                    duration_ms=round(duration, 2),

                    repository_updated=False

                )

                #
                # Console Output
                #

                ConsoleLogger.success(

                    engine="Repository",

                    original=locator,

                    recovered=alt,

                    duration=duration,

                    confidence=100,

                    provider="Repository"

                )

                ConsoleLogger.finished()

                return element

            except TimeoutException:

                LocatorRepository.record_failure(

                    by,

                    value,

                    alt

                )

        ConsoleLogger.failed(

            "Repository"

        )

        return None