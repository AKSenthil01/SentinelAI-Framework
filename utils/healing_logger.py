import json
import os
from datetime import datetime


class HealingLogger:

    LOG_FILE = os.path.join("reports", "healing_log.json")

    @classmethod
    def clear(cls):
        """
        Clear healing log before every test.
        """
        os.makedirs("reports", exist_ok=True)

        with open(cls.LOG_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

        print("\nHealing log cleared.")

    @classmethod
    def log(
            cls,
            original,
            recovered,
            source,
            provider=None,
            confidence=None,
            reason=None,
            duration_ms=None,
            repository_updated=False,
            test=None,
            page=None
    ):

        os.makedirs("reports", exist_ok=True)

        entry = {

            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "test": test,

            "page": page,

            "original": str(original),

            "recovered": str(recovered),

            "source": source,

            "provider": provider,

            "confidence": confidence,

            "reason": reason,

            "duration_ms": duration_ms,

            "repository_updated": repository_updated

        }

        #
        # Load previous log
        #

        logs = []

        if os.path.exists(cls.LOG_FILE):

            try:

                with open(cls.LOG_FILE, "r", encoding="utf-8") as f:

                    logs = json.load(f)

            except Exception:

                logs = []

        #
        # Append new record
        #

        logs.append(entry)

        #
        # Debug
        #

        print("\nLogger writing to:")
        print(os.path.abspath(cls.LOG_FILE))

        print(f"Entries in log : {len(logs)}")

        #
        # Save
        #

        with open(cls.LOG_FILE, "w", encoding="utf-8") as f:

            json.dump(logs, f, indent=4)

    @classmethod
    def get_logs(cls):

        if not os.path.exists(cls.LOG_FILE):
            return []

        try:

            with open(cls.LOG_FILE, "r", encoding="utf-8") as f:

                return json.load(f)

        except Exception:

            return []