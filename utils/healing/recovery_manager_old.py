"""
Enterprise Recovery Manager

Responsibilities
----------------
✔ Execute recovery engines in order
✔ Stop at first successful recovery
✔ Update Locator Repository
✔ Record success/failure
✔ Write Healing Log
✔ Print console summary

Execution Order

Repository
↓

Strategy

↓

AI
"""

from __future__ import annotations

import time

from utils.healing.console_logger import ConsoleLogger
from utils.healing_logger import HealingLogger
from utils.locator_repository import LocatorRepository

from utils.healing.repository_recovery import RepositoryRecovery
from utils.healing.strategy_recovery import StrategyRecovery
from utils.healing.ai_recovery import AIRecovery


class RecoveryManager:

    def __init__(self):

        self.engines = [

            RepositoryRecovery(),

            StrategyRecovery(),

            AIRecovery()

        ]

    # ---------------------------------------------------------

    def recover(

            self,

            driver,

            wait,

            locator,

            condition

    ):

        for engine in self.engines:

            start = time.perf_counter()

            element = engine.recover(

                driver,

                wait,

                locator,

                condition

            )

            if element is None:

                continue

            duration = (

                time.perf_counter() - start

            ) * 1000

            recovered_locator = getattr(

                engine,

                "recovered_locator",

                None

            )

            provider = getattr(

                engine,

                "provider",

                engine.__class__.__name__

            )

            source = getattr(

                engine,

                "source",

                provider

            )

            confidence = getattr(

                engine,

                "confidence",

                90

            )

            reason = getattr(

                engine,

                "reason",

                ""

            )

            #
            # Learn successful recovery
            #

            if recovered_locator:

                LocatorRepository.add_locator(

                    locator[0],

                    locator[1],

                    recovered_locator,

                    source=source

                )

                LocatorRepository.record_success(

                    locator[0],

                    locator[1],

                    recovered_locator

                )

            #
            # Healing log
            #

            HealingLogger.log(

                original=locator,

                recovered=recovered_locator,

                source=source,

                provider=provider,

                confidence=confidence,

                reason=reason,

                duration_ms=round(duration, 2),

                repository_updated=True

            )

            #
            # Console output
            #

            ConsoleLogger.success(

                engine=provider,

                original=locator,

                recovered=recovered_locator,

                duration=duration,

                confidence=confidence,

                provider=provider

            )

            ConsoleLogger.finished()

            return element

        #
        # Everything failed
        #

        ConsoleLogger.failed("RecoveryManager")

        return None