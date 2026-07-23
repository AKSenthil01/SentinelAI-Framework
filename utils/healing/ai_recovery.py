"""
Enterprise AI Recovery Engine
"""

import time

from selenium.common.exceptions import TimeoutException

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

        ConsoleLogger.trying("AI")

        advisor = AIAdvisorFactory.get_advisor()
        print("AIRecovery STEP-A")
        print(advisor)

        if advisor is None:
            ConsoleLogger.failed("AI")
            return None

        result = advisor.suggest_locators(locator, driver)
        print("AIRecovery STEP-B")
        print(result)

        if result is None:
            ConsoleLogger.failed("AI")
            return None

        confidence = result.get("confidence",0)
        reason = result.get("reason", "")
        locators = result.get("locators", [])

        for recovered_locator in locators:

            start = time.perf_counter()

            try:
                print(f"\nRecovered locator = {recovered_locator}")

                element = wait.until(
                    condition(recovered_locator)
                )

                print("Recovered element:", element)
                print("Driver session:", driver.session_id)

                duration = (
                        time.perf_counter() - start
                ) * 1000

                #

                print("\nSTEP-C : Before add_locator")

                LocatorRepository.add_locator(
                    locator[0],
                    locator[1],
                    recovered_locator,
                    source="AI"
                )

                print(">>>>>>>> add_locator COMPLETED <<<<<<<<")

                print("STEP-D : After add_locator")

                LocatorRepository.record_success(
                    locator[0],
                    locator[1],
                    recovered_locator
                )

                print(">>>>>>>> record_success COMPLETED <<<<<<<<")

                print("STEP-E : After record_success")

                HealingLogger.log(
                    original=locator,
                    recovered=recovered_locator,
                    source="AI",
                    provider="Ollama",
                    confidence=confidence,
                    reason=reason,
                    duration_ms=round(duration, 2),
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

                print(">>>>>>>> RETURNING ELEMENT <<<<<<<<")

                return element


            except Exception as e:

                import traceback

                print("\n========== AIRecovery Exception ==========")

                traceback.print_exc()

                print("=========================================")


                raise

                LocatorRepository.record_failure(
                    locator[0],
                    locator[1],
                    recovered_locator
                )

        ConsoleLogger.failed("AI")

        return None