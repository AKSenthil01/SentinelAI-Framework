class AISession:

    last_prompt = ""

    last_response = ""

    @classmethod
    def save(cls, prompt, response):

        cls.last_prompt = prompt

        cls.last_response = response