"""
Enterprise Test Data Generator

Reusable across

✓ UI Tests
✓ API Tests
✓ Hybrid Tests
✓ Performance Tests
"""

from faker import Faker

fake = Faker("en_IN")


class DataGenerator:

    # -----------------------------------------------------

    @staticmethod
    def create_user():

        return {

            "name": fake.name(),

            "email": fake.unique.email(),

            "password": "Password@123",

            "title": "Mr",

            "birth_date": str(
                fake.random_int(
                    min=1,
                    max=28
                )
            ),

            "birth_month": str(
                fake.random_int(
                    min=1,
                    max=12
                )
            ),

            "birth_year": str(
                fake.random_int(
                    min=1985,
                    max=2000
                )
            ),

            "firstname": fake.first_name(),

            "lastname": fake.last_name(),

            "company": fake.company(),

            "address1": fake.street_address(),

            "address2": "",

            "country": "India",

            "zipcode": fake.postcode(),

            "state": fake.state(),

            "city": fake.city(),

            "mobile_number": fake.msisdn()[:10]

        }

    # -----------------------------------------------------

    @staticmethod
    def create_login():

        user = DataGenerator.create_user()

        return {

            "email": user["email"],

            "password": user["password"]

        }

    # -----------------------------------------------------

    @staticmethod
    def random_product_quantity():

        return fake.random_int(

            min=1,

            max=5

        )

    # -----------------------------------------------------

    @staticmethod
    def random_search_keyword():

        keywords = [

            "Top",

            "Dress",

            "Shirt",

            "Jeans",

            "Tshirt",

            "Saree"

        ]

        return fake.random_element(

            keywords

        )