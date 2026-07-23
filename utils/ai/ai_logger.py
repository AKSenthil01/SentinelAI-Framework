from pathlib import Path
from datetime import datetime

LOG = Path("reports/ai_recovery.log")


class AILogger:

    @staticmethod
    def clear():
        LOG.parent.mkdir(exist_ok=True)

        LOG.write_text("")

    @staticmethod
    def write(title, content):

        with LOG.open(
                "a",
                encoding="utf-8"
        ) as f:

            f.write("\n")
            f.write("=" * 80)
            f.write("\n")

            f.write(title)

            f.write("\n")
            f.write("=" * 80)
            f.write("\n")

            f.write(str(content))

            f.write("\n")