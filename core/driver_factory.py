# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# def get_driver():
#     options = Options()
#     options.add_argument("--headless=new")   # Required for GitHub Action
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#     return driver

from selenium import webdriver
import os

def get_driver(browser="chrome"):
    options = webdriver.ChromeOptions()

    # Detect CI environment
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver