import pytest

from utils.api.api_client import ApiClient
from utils.api.response_validator import ResponseValidator


@pytest.mark.api
class TestDeleteAccountAPI:

    def test_delete_account(self, created_user):
        """
        Verify Delete Account API
        """

        response = ApiClient.delete(

            "/deleteAccount",

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

        print("=" * 70)

        print("ACCOUNT DELETED SUCCESSFULLY")

        print("=" * 70)

        print("Email :", created_user["email"])