import pytest

from utils.api.api_client import ApiClient
from utils.api.response_validator import ResponseValidator


@pytest.mark.api
class TestVerifyLoginAPI:

    def test_verify_login(self, created_user):

        response = ApiClient.post(

            "/verifyLogin",

            data={

                "email": created_user["email"],

                "password": created_user["password"]

            }

        )

        ResponseValidator.validate_status(

            response,

            200

        )

        data = response.json()

        assert data["responseCode"] == 200

        print()

        print("=" * 60)

        print("LOGIN VERIFIED")

        print("=" * 60)

        print("Email :", created_user["email"])