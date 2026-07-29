"""
Ranks candidate DOM elements before sending them to Ollama.
"""

import re
from difflib import SequenceMatcher
from bs4 import BeautifulSoup


class CandidateRanker:

    MAX_RESULTS = 8

    IMPORTANT_ATTRIBUTES = [

        "id",
        "name",
        "data-qa",
        "data-testid",
        "aria-label",
        "placeholder",
        "title",
        "href",
        "value"

    ]

    @staticmethod
    def rank(html, locator):

        if not html:
            return ""

        soup = BeautifulSoup(html, "html.parser")

        _, locator_value = locator

        tokens = CandidateRanker.tokenize(locator_value)

        scored = []

        for element in soup.find_all(True):

            score = CandidateRanker.compute_score(
                element,
                tokens
            )

            if score > 0:

                scored.append(

                    (

                        score,

                        str(element)

                    )

                )

        scored.sort(

            key=lambda x: x[0],

            reverse=True

        )

        result = []

        for _, item in scored[:CandidateRanker.MAX_RESULTS]:

            result.append(item)

        return "\n\n".join(result)

    @staticmethod
    def tokenize(text):

        return re.findall(

            r"[A-Za-z0-9]+",

            text.lower()

        )

    @staticmethod
    def similarity(a, b):

        return SequenceMatcher(

            None,

            a.lower(),

            b.lower()

        ).ratio()

    @staticmethod
    def compute_score(element, tokens):

        score = 0

        values = []

        for attr in CandidateRanker.IMPORTANT_ATTRIBUTES:

            value = element.get(attr)

            if value:

                values.append(str(value))

        if element.get("class"):

            values.append(

                " ".join(element.get("class"))

            )

        text = element.get_text(

            " ",

            strip=True

        )

        if text:

            values.append(text)

        for token in tokens:

            for value in values:

                score += CandidateRanker.similarity(

                    token,

                    value

                )

        return score