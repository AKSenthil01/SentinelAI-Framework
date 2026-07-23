"""
Enterprise Console Logger
"""

from datetime import datetime


class ConsoleLogger:

    LINE = "=" * 70

    @staticmethod
    def started(locator):

        print()

        print(ConsoleLogger.LINE)

        print("SELF HEALING ACTIVATED")

        print(ConsoleLogger.LINE)

        print(

            f"Time : {datetime.now().strftime('%H:%M:%S')}"

        )

        print(

            f"Original Locator : {locator}"

        )

        print()

    @staticmethod
    def trying(engine):

        print(

            f"Trying {engine} Recovery..."

        )

    @staticmethod
    def success(

            engine,

            original,

            recovered,

            duration,

            confidence=None,

            provider=None

    ):

        print()

        print("SUCCESS")

        print("-" * 70)

        print(

            f"Recovery Engine : {engine}"

        )

        if provider:

            print(

                f"Provider : {provider}"

            )

        print(

            f"Original Locator : {original}"

        )

        print(

            f"Recovered Locator : {recovered}"

        )

        if confidence is not None:

            print(

                f"Confidence : {confidence}%"

            )

        print(

            f"Recovery Time : {duration:.2f} ms"

        )

        print(ConsoleLogger.LINE)

    @staticmethod
    def failed(engine):

        print(

            f"✗ {engine} Recovery Failed"

        )

    @staticmethod
    def finished():

        print()

        print(

            "Test Execution Continued Successfully"

        )

        print(ConsoleLogger.LINE)

        print()