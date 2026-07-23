import pytest

from utils.api.api_client import ApiClient
from utils.api.response_validator import ResponseValidator


@pytest.mark.api
class TestGetUserDetailsAPI:

    def test_get_user_details(self, created_user):
        """
        Verify Get User Details API
        """

        response = ApiClient.get(

            "/getUserDetailByEmail",

            params={

                "email": created_user["email"]

            }

        )

        ResponseValidator.validate_status(

            response,

            200

        )

        data = response.json()

        assert data["responseCode"] == 200

        assert data["user"]["email"] == created_user["email"]

        print()

        print("=" * 70)

        print("USER DETAILS VERIFIED")

        print("=" * 70)

        print("Name  :", data["user"]["name"])

        print("Email :", data["user"]["email"])

        print("=" * 70)