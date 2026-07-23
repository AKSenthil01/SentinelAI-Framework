# test_browser_versions.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

print("Browser Version:")
print(driver.capabilities["browserVersion"])

print("\nChromeDriver Version:")
print(driver.capabilities["chrome"]["chromedriverVersion"])

input("\nPress Enter to close...")

driver.quit()