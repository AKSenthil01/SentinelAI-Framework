"""
Enterprise Self-Healing Orchestrator

Recovery Flow

1. Original Locator
2. Repository Recovery
3. Strategy Recovery
4. Fuzzy Recovery
5. AI Recovery
"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from utils.self_healing_config import (
    SELF_HEALING_ENABLED,
    SELF_HEALING_DEMO
)

from utils.healing.console_logger import ConsoleLogger
from utils.healing.repository_recovery import RepositoryRecovery
from utils.healing.strategy_recovery import StrategyRecovery
from utils.healing.fuzzy_recovery import FuzzyRecovery
from utils.healing.ai_recovery import AIRecovery


class SelfHealing:

    repository = RepositoryRecovery()

    strategy = StrategyRecovery()

    fuzzy = FuzzyRecovery()

    ai = AIRecovery()

    # ----------------------------------------------------------

    @staticmethod
    def find(

            driver,

            wait,

            locator,

            condition

    ):

        return SelfHealing._find_with_condition(

            driver,

            wait,

            locator,

            condition

        )

    # ----------------------------------------------------------

    @staticmethod
    def find_all(

            driver,

            wait,

            locator

    ):

        return SelfHealing._find_with_condition(

            driver,

            wait,

            locator,

            EC.presence_of_all_elements_located

        )

    # ----------------------------------------------------------

    @staticmethod
    def _find_with_condition(

            driver,

            wait,

            locator,

            condition

    ):

        #
        # Validate locator
        #

        if (

                not isinstance(locator, tuple)

                or

                len(locator) != 2

        ):

            raise TypeError(

                f"Invalid locator : {locator}"

            )

        #
        # Try Original Locator
        #

        try:

            if not SELF_HEALING_DEMO:

                return wait.until(

                    condition(locator)

                )

            ConsoleLogger.started(locator)

        except TimeoutException:

            pass

        #
        # Self Healing Disabled
        #

        if not SELF_HEALING_ENABLED:

            raise TimeoutException(

                f"Unable to locate : {locator}"

            )

        #
        # Repository Recovery
        #

        element = SelfHealing.repository.recover(

            driver,

            wait,

            locator,

            condition

        )

        if element:

            return element

        #
        # Strategy Recovery
        #

        element = SelfHealing.strategy.recover(

            driver,

            wait,

            locator,

            condition

        )

        if element:

            return element

        #
        # Fuzzy Recovery
        #

        element = SelfHealing.fuzzy.recover(

            driver,

            wait,

            locator,

            condition

        )

        if element:

            return element

        #
        # AI Recovery
        #

        element = SelfHealing.ai.recover(

            driver,

            wait,

            locator,

            condition

        )

        if element:

            return element

        #
        # Nothing Worked
        #

        raise TimeoutException(

            f"Unable to recover locator : {locator}"

        )