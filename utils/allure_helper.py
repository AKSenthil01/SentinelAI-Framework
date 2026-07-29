import json
import os
import allure


class AllureHelper:

    @staticmethod
    def attach_json(file_path, name):

        if os.path.exists(file_path):

            allure.attach.file(
                file_path,
                name=name,
                attachment_type=allure.attachment_type.JSON
            )

    @staticmethod
    def attach_html(file_path, name):

        if os.path.exists(file_path):

            allure.attach.file(
                file_path,
                name=name,
                attachment_type=allure.attachment_type.HTML
            )

    @staticmethod
    def attach_text(text, name):

        allure.attach(
            text,
            name=name,
            attachment_type=allure.attachment_type.TEXT
        )

    @staticmethod
    def attach_png(driver, name):

        allure.attach(
            driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @staticmethod
    def attach_prompt(prompt):

        if prompt:
            allure.attach(
                prompt,
                name="AI Prompt",
                attachment_type=allure.attachment_type.TEXT
            )

    # @staticmethod
    # def attach_response(response):
    #
    #     if response:
    #         allure.attach(
    #             response,
    #             name="AI Response",
    #             attachment_type=allure.attachment_type.TEXT
    #         )


    @staticmethod
    def attach_response(response):

        if response is None:
            return

        if isinstance(response, dict):
            response = json.dumps(response, indent=2)

        elif not isinstance(response, str):
            response = str(response)

        allure.attach(
            response,
            name="AI Response",
            attachment_type=allure.attachment_type.TEXT
        )