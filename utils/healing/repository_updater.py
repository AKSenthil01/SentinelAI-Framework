"""
Repository Updater

Automatically stores
successful AI recoveries.

Enterprise behaviour:
AI learns permanently.
"""

import json
import os


class RepositoryUpdater:

    FILE = "locator_repository.json"

    @classmethod
    def update(
            cls,
            failed_locator,
            recovered_locator
    ):

        if os.path.exists(cls.FILE):

            with open(cls.FILE, encoding="utf-8") as f:

                repo = json.load(f)

        else:

            repo = {}

        key = str(failed_locator)

        repo[key] = {

            "primary": list(recovered_locator),

            "confidence": 100,

            "source": "AI"

        }

        with open(
                cls.FILE,
                "w",
                encoding="utf-8"
        ) as f:

            json.dump(
                repo,
                f,
                indent=4
            )

        print()

        print("Repository updated.")

        print(failed_locator)

        print("→")

        print(recovered_locator)

        print()