from selenium import webdriver

from utils.ai.ai_factory import AIAdvisorFactory

driver = webdriver.Chrome()

driver.get("https://automationexercise.com/payment")

advisor = AIAdvisorFactory.get_advisor()

xpath = advisor.suggest_locator(
    ("id", "submit123"),
    driver
)

print(xpath)

driver.quit()