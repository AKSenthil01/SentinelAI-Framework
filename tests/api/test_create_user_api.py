import pytest

from utils.api.api_client import ApiClient
from utils.api.response_validator import ResponseValidator
from utils.data_generator.data_generator import DataGenerator
from utils.context.test_context import TestContext


@pytest.mark.api
class TestCreateUserAPI:

    def test_create_account(self):
        """
        Verify Create Account API
        """

        user = DataGenerator.create_user()

        TestContext.set(

            "current_user",

            user

        )

        response = ApiClient.post(

            "/createAccount",

            data=user

        )

        ResponseValidator.validate_status(

            response,

            200

        )

        data = response.json()

        assert data["responseCode"] == 201

        print()

        print("=" * 70)

        print("ACCOUNT CREATED SUCCESSFULLY")

        print("=" * 70)

        print(f"Name     : {user['name']}")
        print(f"Email    : {user['email']}")
        print(f"Company  : {user['company']}")
        print(f"City     : {user['city']}")
        print("=" * 70)