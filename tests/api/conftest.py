import pytest

from utils.api.api_client import ApiClient
from utils.api.response_validator import ResponseValidator
from utils.data_generator.data_generator import DataGenerator


@pytest.fixture
def created_user():

    user = DataGenerator.create_user()

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

    yield user