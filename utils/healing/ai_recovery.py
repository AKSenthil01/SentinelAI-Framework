import time

from selenium.common.exceptions import TimeoutException

from utils.allure_helper import AllureHelper
from utils.healing.healing_base import HealingBase
from utils.healing.console_logger import ConsoleLogger
from utils.ai.ai_factory import AIAdvisorFactory
from utils.healing_logger import HealingLogger
from utils.locator_repository import LocatorRepository


class AIRecovery(HealingBase):

    def recover(

            self,

            driver,

            wait,

            locator,

            condition

    ):
        # Don't learn obviously unrelated elements
        if locator[0] == "xpath" and "Download Invoice" in locator[1]:
            ConsoleLogger.failed("AI")
            return None

        ConsoleLogger.trying("AI")

        advisor = AIAdvisorFactory.get_advisor()

        if advisor is None:
            ConsoleLogger.failed("AI")
            return None

        result = advisor.suggest_locators(locator, driver)

        if result is None:
            ConsoleLogger.failed("AI")
            return None

        confidence = result.get("confidence", 0)
        reason = result.get("reason", "")
        locators = result.get("locators", [])

        for recovered_locator in locators:

            start = time.perf_counter()

            try:

                element = wait.until(
                    condition(recovered_locator)
                )

                duration = (
                        time.perf_counter() - start
                ) * 1000


                #recovered_locator
                # Repository update only AFTER successful recovery
                #

                LocatorRepository.add_locator(

                    locator[0],

                    locator[1],

                    recovered_locator,

                    source="AI"

                )

                AllureHelper.attach_text(
                    str(recovered_locator),
                    "Recovered Locator"
                )

                AllureHelper.attach_text(
                    "AI Recovery (Ollama)",
                    "Recovery Engine"
                )

                LocatorRepository.record_success(

                    locator[0],

                    locator[1],

                    recovered_locator

                )

                HealingLogger.log(

                    original=locator,

                    recovered=recovered_locator,

                    source="AI",

                    provider="Ollama",

                    confidence=confidence,

                    reason=reason,

                    duration_ms=duration,

                    repository_updated=True

                )

                ConsoleLogger.success(

                    engine="AI",

                    original=locator,

                    recovered=recovered_locator,

                    duration=duration,

                    confidence=confidence,

                    provider="Ollama"

                )


                ConsoleLogger.finished()

                return element

            except Exception:

                LocatorRepository.record_failure(

                    locator[0],

                    locator[1],

                    recovered_locator

                )

                continue

        ConsoleLogger.failed("AI")

        return None