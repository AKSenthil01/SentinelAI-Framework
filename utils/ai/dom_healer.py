from utils.ai.dom_similarity import DOMSimilarity
from utils.ai.dom_matcher import DOMMatcher


class DOMHealer:

    @staticmethod
    def recover(driver, original_locator):

        candidates = DOMSimilarity.find_candidates(driver)

        return DOMMatcher.best_locator(

            original_locator,

            candidates

        )