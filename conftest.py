import json
import os
from datetime import datetime

import allure
from faker import Faker
#import undetected_chromedriver as uc
import pytest
import pytest_html
#import uc
from dotenv import load_dotenv
from selenium import webdriver
import random
import string
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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

    # CONDITIONAL HEADLESS (KEY PART)
    if os.getenv("CI") == "true":
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

    # Use WebDriver Manager (recommended)
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.maximize_window()

    yield driver

    driver.quit()


#@pytest.fixture
# def random_name():
#     """Generates a random email ID for testing."""
#     username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
#     return username
@pytest.fixture(autouse=True)
def random_name():
    """Generates a random name for testing."""
    # fake=faker.Faker()
    username = fake.name()
    #username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return username

@pytest.fixture
def existing_user():
    with open("test_data/user.json") as f:
        data = json.load(f)
    return data

# @pytest.fixture
# def random_email():
#     """Generates a random email ID for testing."""
#     username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
#     email = f"test_{username}@example.com"
#     with open("test_data/user.json", "w") as f:
#         json.dump(email, f)
#     return email

@pytest.fixture()
def random_email():
    """Generates a random email ID for testing."""
    # username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    # email = f"test_{username}@example.com"
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
    """
    Extends the Pytest-HTML report to include screenshots on failure.
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.failed or xfail):
            # 1. Get the driver instance from the test item
            driver = item.funcargs['setup']

            # 2. Define screenshot name and path
            file_name = f"Screenshot_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.png"
            reports_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            if not os.path.exists(reports_dir):
                os.makedirs(reports_dir)

            file_path = os.path.join(reports_dir, file_name)

            # 3. Capture the screenshot
            driver.save_screenshot(file_path)

            allure.attach(driver.get_screenshot_as_png(),
                          name="Failure screenshot",
                          attachment_type=allure.attachment_type.PNG
                          )

            # 4. Attach to HTML report
            if file_path:
                html = '<div><img src="screenshots/%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_addoption(parser):
    # This tells pytest how to read the custom line from pytest.ini
    parser.addini("base_url", help="Base URL for the application")


