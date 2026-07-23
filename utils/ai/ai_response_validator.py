import re


class AIResponseValidator:
    """
    Validates AI-generated Selenium locators before
    they are used by Selenium.
    """

    MIN_LENGTH = 8

    @staticmethod
    def is_valid_xpath(xpath):

        if xpath is None:
            return False

        xpath = xpath.strip()

        #
        # Empty
        #

        if xpath == "":
            return False

        #
        # Too short
        #

        if len(xpath) < AIResponseValidator.MIN_LENGTH:
            return False

        #
        # Must begin with //
        #

        if not xpath.startswith("//"):
            return False

        #
        # Avoid absolute XPath
        #

        if xpath.startswith("/html"):
            return False

        #
        # Avoid body XPath
        #

        if xpath.startswith("//body"):
            return False

        #
        # Spaces only
        #

        if xpath.isspace():
            return False

        #
        # Markdown
        #

        if "```" in xpath:
            return False

        #
        # Explanation text
        #

        if xpath.lower().startswith("suggest"):
            return False

        #
        # AI sometimes returns English
        #

        if re.search(
                r"[A-Za-z]{20,}",
                xpath
        ):
            return False

        return True