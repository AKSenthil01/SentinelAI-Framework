import pathlib

from pages.demo.ai_demo_page import AIDemoPage

from utils.locator_repository import LocatorRepository

from utils.healing_logger import HealingLogger


class TestAIDemo:

    def test_ai_demo(self, driver):

        LocatorRepository.clear()

        HealingLogger.clear()

        page = AIDemoPage(driver)

        demo = pathlib.Path(
            "demo/ai_demo.html"
        ).resolve().as_uri()

        page.open(demo)

        page.click_place_order()