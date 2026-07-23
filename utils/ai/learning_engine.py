from utils.locator_repository import LocatorRepository
from utils.healing_logger import HealingLogger
from utils.ai.confidence_score import ConfidenceScore


class LearningEngine:

    @staticmethod
    def learn(original, recovered, source):

        LocatorRepository.add_locator(
            original[0],
            original[1],
            recovered,
            source = source
        )

        LocatorRepository.record_success(
            original[0],
            original[1],
            recovered
        )

        HealingLogger.log(
            original=original,
            recovered=recovered,
            source=source,
            confidence=ConfidenceScore.calculate(recovered)
        )