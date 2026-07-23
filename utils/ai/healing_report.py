class HealingReport:

    @staticmethod
    def print_summary(
            original,
            recovered,
            source,
            duration,
            provider=None
    ):

        print()

        print("=" * 65)

        print("        ENTERPRISE SELF-HEALING REPORT")

        print("=" * 65)

        print(f"Original Locator : {original}")

        print(f"Recovered Locator: {recovered}")

        print(f"Recovery Source  : {source}")

        if provider:
            print(f"AI Provider      : {provider}")

        print(f"Recovery Time    : {duration} ms")

        print("Repository Learn : YES")

        print("Status           : SUCCESS")

        print("=" * 65)

        print()