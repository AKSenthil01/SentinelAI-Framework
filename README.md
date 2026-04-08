# **Automation Exercise - Selenium Python Framework**
## **🚀Project Overview**
This repository contains a professional-grade automation framework designed to validate e-commerce workflows on the `automationexercise.com` platform. It demonstrates modern SDET practices, focusing on maintainability, scalability, and clean code.
## 🛠 Tech Stack
* **Language:** Python 3.x
* **Framework:** Pytest
* **Library:** Selenium WebDriver
* **Design Pattern**: Page Object Model (POM)
* **Reporting:** Pytest-HTML / Screenshot on Failure

# 🏗 Key Features
* **Modular Architecture:** Separated Test Logic, Page Actions, and Locators.
* **Smart Setup/Teardown:** Managed via Pytest Fixtures in `conftest.py`.
* **Auto-Screenshot:** Automatically captures browser state on test failure for rapid debugging.
* **Resilient Locators:** Strategic use of CSS Selectors and XPaths to minimize script brittleness.

## 🚦 How to Run
* pip install -r requirements.txt
* pytest --html=reports/report.html

## Future Enhancements
* CI/CD integration (GitHub Actions)
* Parallel execution (pytest-xdist)
* Docker execution

