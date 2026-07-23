from selenium.webdriver.common.by import By


class DOMMatcher:

    @staticmethod
    def similarity(original_locator, candidate):

        score = 0

        by, value = original_locator

        if candidate["id"]:

            if value.lower() in candidate["id"].lower():

                score += 60

        if candidate["name"]:

            if value.lower() in candidate["name"].lower():

                score += 50

        if candidate["text"]:

            if value.lower() in candidate["text"].lower():

                score += 30

        if candidate["class"]:

            if value.lower() in candidate["class"].lower():

                score += 20

        return score

    @staticmethod
    def best_locator(original_locator, candidates):

        ranked = sorted(

            candidates,

            key=lambda c: DOMMatcher.similarity(original_locator, c),

            reverse=True

        )

        if not ranked:

            return None

        best = ranked[0]

        if DOMMatcher.similarity(original_locator, best) < 40:

            return None

        #
        # Build locator
        #

        if best["id"]:

            return (By.ID, best["id"])

        if best["name"]:

            return (By.NAME, best["name"])

        if best["text"]:

            return (

                By.XPATH,

                f"//*[contains(text(),'{best['text']}')]"

            )

        return None