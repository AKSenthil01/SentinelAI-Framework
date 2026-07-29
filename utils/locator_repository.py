import json
import os
from datetime import datetime


class LocatorRepository:
    """
    Enterprise Knowledge Repository

    Stores:

    Original Locator
            │
            ▼
    Alternatives
            │
            ▼
    Success Count
            │
            ▼
    Failure Count
            │
            ▼
    Confidence
            │
            ▼
    Last Used
            │
            ▼
    Source Engine
    """

    FILE_PATH = r"repository\locator_repository.json"

    repository = {}

    # ---------------------------------------------------------

    @classmethod
    def load_repository(cls):

        if not os.path.exists(cls.FILE_PATH):

            cls.repository = {}

            cls.save_repository()

            return

        try:

            with open(cls.FILE_PATH, "r", encoding="utf-8") as f:

                content = f.read().strip()

                if not content:

                    cls.repository = {}

                    return

                cls.repository = json.loads(content)

        except Exception:

            cls.repository = {}

    # ---------------------------------------------------------

    @classmethod
    def save_repository(cls):

        with open(cls.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(

                cls.repository,

                f,

                indent=4

            )# ---------------------------------------------------------

    @staticmethod
    def _key(by, value):

        return f"{by}::{value}"

    # ---------------------------------------------------------

    @classmethod
    def add_locator(

            cls,

            by,

            value,

            locator,

            source="Unknown"

    ):
        print("ENTERED add_locator()")

        print("1")
        cls.initialize()

        print("2")
        key = cls._key(by, value)

        print("3", key)

        if key not in cls.repository:
            print("4")

            cls.repository[key] = {
                "alternatives": []
            }

        print("5")

        alternatives = cls.repository[key]["alternatives"]

        print("6")

        locator = list(locator)

        print("7", locator)

        for item in alternatives:

            print("8")

            if item["locator"] == locator:
                return

        print("9")

        try:
            alternatives.append(
                {
                    "locator": locator,
                    "source": source,
                    "success": 0,
                    "failure": 0,
                    "confidence": 0,
                    "last_used": None
                }
            )

            print("11")

            print(type(cls.save_repository))
            print(cls.save_repository)

            cls.save_repository()

            print("12")

        except Exception as e:

            import traceback

            print("\n========== add_locator EXCEPTION ==========")
            traceback.print_exc()
            print("===========================================")

            raise

    # ---------------------------------------------------------

    @classmethod
    def record_success(

            cls,

            by,

            value,

            locator

    ):
        cls.initialize()

        cls._update_stats(

            by,

            value,

            locator,

            success=True

        )

    # ---------------------------------------------------------

    @classmethod
    def record_failure(

            cls,

            by,

            value,

            locator

    ):
        cls.initialize()

        cls._update_stats(

            by,

            value,

            locator,

            success=False

        )

    # ---------------------------------------------------------

    @classmethod
    def _update_stats(

            cls,

            by,

            value,

            locator,

            success

    ):

        key = cls._key(by, value)

        locator = list(locator)

        if key not in cls.repository:

            return

        alternatives = cls.repository[key]["alternatives"]

        for item in alternatives:

            if item["locator"] != locator:

                continue

            if success:

                item["success"] += 1

            else:

                item["failure"] += 1

            total = item["success"] + item["failure"]

            if total:

                item["confidence"] = round(

                    item["success"] / total * 100,

                    2

                )

            item["last_used"] = datetime.now().strftime(

                "%Y-%m-%d %H:%M:%S"

            )

            break

        cls.save_repository()

    # ---------------------------------------------------------

    @classmethod
    def get_alternatives(

            cls,

            by,

            value

    ):
        cls.initialize()

        key = cls._key(by, value)

        if key not in cls.repository:

            return []

        alternatives = cls.repository[key]["alternatives"]

        alternatives = sorted(

            alternatives,

            key=lambda x: x["confidence"],

            reverse=True

        )

        return [

            tuple(item["locator"])

            for item in alternatives

        ]

    # ---------------------------------------------------------

    @classmethod
    def dump(cls):

        return cls.repository

    # ---------------------------------------------------------

    @classmethod
    def initialize(cls):
        """
        Load repository only once.
        """
        if not cls.repository:
            cls.load_repository()