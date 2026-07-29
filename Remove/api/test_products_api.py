import pytest

from utils.api.api_client import ApiClient
from utils.api.response_validator import ResponseValidator


@pytest.mark.api
class TestProductsAPI:

    def test_get_products_list(self):
        """
        Verify Products List API
        """

        response = ApiClient.get(
            "/productsList"
        )

        #
        # Status Code
        #

        ResponseValidator.validate_status(
            response,
            200
        )

        #
        # Response should contain products
        #

        data = response.json()

        assert "products" in data

        assert len(data["products"]) > 0

        print("\nTotal Products :", len(data["products"]))