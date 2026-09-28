import json
from datetime import datetime
import allure
from faker import Faker
import pytest_html
from dotenv import load_dotenv
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.healing_dashboard import HealingDashboard
from utils.api.api_client import ApiClient
from utils.api.response_validator import ResponseValidator
from utils.data_generator.data_generator import DataGenerator
fake=Faker()

@pytest.fixture
def setup():
    # Define download directory
    download_dir = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    chrome_options = webdriver.ChromeOptions()

    # Chrome preferences
    prefs = {
        "profile.default_content_settings.popups": 0,
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.page_load_strategy = 'eager'

    # CI
    if os.getenv("CI") == "true":
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")


    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()

@pytest.fixture
def driver(setup):
    return setup

@pytest.fixture
def test_data():
    """
    Loads static test data from test_data/test_data.json
    """

    file_path = os.path.join(
        os.getcwd(),
        "test_data",
        "test_data.json"
    )

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture
def random_name():
    """Generates a random name for testing."""
    username = fake.name()
    return username

@pytest.fixture
def existing_user():
    with open("test_data/user.json") as f:
        data = json.load(f)
    return data

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

@pytest.fixture
def random_email():
    """Generates a random email ID for testing."""
    email = fake.email()
    with open("test_data/user.json", "w") as f:
        json.dump(email, f)
    return email

def pytest_configure(config):
    # This loads the .env file globally for the entire test session
    load_dotenv()

@pytest.fixture
def payment_data():
    """
    Provides credit card data to any test that requests it.
    """
    return {
        "name": os.getenv("CARD_NAME"),
        "number": os.getenv("CARD_NUMBER"),
        "cvc": os.getenv("CARD_CVC"),
        "month": os.getenv("CARD_EXP_MONTH"),
        "year": os.getenv("CARD_EXP_YEAR")
    }

@pytest.fixture
def reg_password():
    return os.getenv("REG_PASSWORD")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when in ("setup", "call"):

        xfail = hasattr(report, "wasxfail")

        if report.failed or xfail:

            driver = item.funcargs.get("driver")

            if driver:

                reports_dir = os.path.join(
                    os.getcwd(),
                    "reports",
                    "screenshots"
                )

                os.makedirs(reports_dir, exist_ok=True)

                file_name = (
                    f"Screenshot_"
                    f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.png"
                )

                file_path = os.path.join(
                    reports_dir,
                    file_name
                )

                driver.save_screenshot(file_path)

                #
                # Attach to Allure
                #

                if os.path.exists(file_path):

                    allure.attach.file(
                        file_path,
                        name="Failure Screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )

                    #
                    # Attach to HTML Report
                    #

                    html = (
                        f'<div>'
                        f'<img src="screenshots/{file_name}" '
                        f'style="width:304px;height:228px;" '
                        f'onclick="window.open(this.src)"/>'
                        f'</div>'
                    )

                    extra.append(
                        pytest_html.extras.html(html)
                    )

    report.extra = extra

def pytest_addoption(parser):
    # This tells pytest how to read the custom line from pytest.ini
    parser.addini("base_url", help="Base URL for the application")


def pytest_sessionfinish(session, exitstatus):
    HealingDashboard.generate()
