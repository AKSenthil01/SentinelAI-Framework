from selenium.webdriver.common.by import By


class DOMSimilarity:

    @staticmethod
    def find_candidates(driver):

        elements = driver.find_elements(By.XPATH, "//*")

        candidates = []

        for element in elements:

            try:

                candidates.append({

                    "tag": element.tag_name,

                    "id": element.get_attribute("id"),

                    "name": element.get_attribute("name"),

                    "class": element.get_attribute("class"),

                    "text": element.text.strip(),

                    "type": element.get_attribute("type"),

                    "element": element

                })

            except Exception:

                pass

        return candidates