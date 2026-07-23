"""
Enterprise Test Context

Stores runtime data shared across

✓ API Tests
✓ UI Tests
✓ Hybrid Tests

Example

TestContext.set("current_user", user)

user = TestContext.get("current_user")
"""


class TestContext:

    _context = {}

    # -----------------------------------------------------

    @classmethod
    def set(

            cls,

            key,

            value

    ):

        cls._context[key] = value

    # -----------------------------------------------------

    @classmethod
    def get(

            cls,

            key,

            default=None

    ):

        return cls._context.get(

            key,

            default

        )

    # -----------------------------------------------------

    @classmethod
    def remove(

            cls,

            key

    ):

        if key in cls._context:

            del cls._context[key]

    # -----------------------------------------------------

    @classmethod
    def clear(cls):

        cls._context.clear()

    # -----------------------------------------------------

    @classmethod
    def dump(cls):

        return cls._context