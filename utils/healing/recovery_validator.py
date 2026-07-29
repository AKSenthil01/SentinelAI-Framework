"""
Recovery Validator

Checks whether the recovered element is
semantically similar to the original one.
"""

from selenium.common.exceptions import NoSuchElementException
from difflib import SequenceMatcher

class RecoveryValidator:

    IMPORTANT_ATTRS = [

        "data-qa",
        "data-testid",
        "aria-label",
        "placeholder"

    ]

    @staticmethod
    def validate(driver, original_locator, recovered_locator):

        #
        # Recovered locator must exist.
        #

        try:

            recovered = driver.find_element(*recovered_locator)

        except NoSuchElementException:

            print("\nRecovered locator not found.")

            return False

        #
        # Original locator intentionally broken?
        #

        try:

            original = driver.find_element(*original_locator)

        except NoSuchElementException:

            print("\nOriginal locator is broken.")
            print("Skipping semantic comparison.")

            return True

        #
        # Same HTML tag?
        #

        if original.tag_name != recovered.tag_name:

            print("\nTag mismatch.")

            return False

        #
        # Compare visible text
        #

        original_text = original.text.strip().lower()

        recovered_text = recovered.text.strip().lower()

        if original_text and recovered_text:

            if original_text == recovered_text:

                return True

        #
        # Compare stable attributes
        #

        for attr in RecoveryValidator.IMPORTANT_ATTRS:

            old_text = original.get_attribute(attr)

            new_text = recovered.get_attribute(attr)

            # if old_value and new_value:
            #
            #     if old_value == new_value:
            #
            #         return True
            if old_text and new_text:

                similarity = SequenceMatcher(
                    None,
                    old_text,
                    new_text
                ).ratio()

                if similarity < 0.60:
                    print(
                        f"\nText similarity too low : {similarity}"
                    )

                    return False

        #
        # Compare button value
        #

        old_value = original.get_attribute("value")

        new_value = recovered.get_attribute("value")

        if old_value and new_value:

            if old_value == new_value:

                if recovered.tag_name.lower() in ("i", "svg"):
                    return False

                text = recovered.text.strip()

                href = recovered.get_attribute("href")

                if not text and not href:
                    return False

                return True

        print("\nSemantic validation failed.")

        return False