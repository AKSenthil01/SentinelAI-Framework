from selenium.common.exceptions import TimeoutException


class CandidateValidator:

    @staticmethod
    def validate(wait, candidates, condition):

        for locator in candidates:

            try:

                element = wait.until(
                    condition(locator)
                )

                return locator, element

            except TimeoutException:

                continue

        return None, None