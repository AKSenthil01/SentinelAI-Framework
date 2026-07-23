"""
Enterprise Healing Logger

Stores every self-healing event.

Used by

- Dashboard
- Analytics
- AI Metrics
- Repository Learning
"""

import json
import os
from datetime import datetime


class HealingLogger:

    LOG_FILE = os.path.join("reports", "healing_log.json")

    # ---------------------------------------------------------

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
            test_name=None,
            page_title=None
    ):

        record = {

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "test": test_name,

            "page": page_title,

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
        # Load existing logs
        #

        logs = []

        if os.path.exists(cls.LOG_FILE):

            try:

                with open(

                        cls.LOG_FILE,

                        "r",

                        encoding="utf-8"

                ) as f:

                    content = f.read().strip()

                    if content:

                        logs = json.loads(content)

            except Exception:

                logs = []

        #
        # Append latest record
        #

        logs.append(record)

        #
        # Save
        #

        with open(

                cls.LOG_FILE,

                "w",

                encoding="utf-8"

        ) as f:

            json.dump(

                logs,

                f,

                indent=4

            )

    # ---------------------------------------------------------

    @classmethod
    def clear(cls):

        with open(

                cls.LOG_FILE,

                "w",

                encoding="utf-8"

        ) as f:

            json.dump(

                [],

                f,

                indent=4

            )