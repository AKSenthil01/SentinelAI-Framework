"""
Reusable Response Validator
"""


class ResponseValidator:

    @staticmethod
    def validate_status(

            response,

            expected_status=200

    ):

        assert (

            response.status_code == expected_status

        ), (

            f"Expected {expected_status}, "

            f"Actual {response.status_code}"

        )

    @staticmethod
    def validate_json(response):

        try:

            return response.json()

        except Exception:

            raise AssertionError(

                "Response is not valid JSON"

            )

    @staticmethod
    def contains(

            response,

            key

    ):

        data = response.json()

        assert key in data, (

            f"{key} not present"

        )