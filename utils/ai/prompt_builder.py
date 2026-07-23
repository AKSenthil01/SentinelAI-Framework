# """
# Enterprise Prompt Builder
#
# Builds deterministic prompts for local LLMs
# like Llama3/Mistral.
#
# The goal is to return ONE Selenium locator only.
# """
#
#
# class PromptBuilder:
#
#     @staticmethod
#     def build_locator_prompt(
#             locator,
#             page_title,
#             page_url,
#             html
#     ):
#
#         by, value = locator
#
#         return f"""
# You are an expert Selenium Automation Engineer.
#
# A Selenium locator has failed.
#
# ====================================================
# PAGE INFORMATION
# ====================================================
#
# Title:
# {page_title}
#
# URL:
# {page_url}
#
# ====================================================
# FAILED LOCATOR
# ====================================================
#
# {by}={value}
#
# ====================================================
# AVAILABLE HTML
# ====================================================
#
# Use ONLY the HTML below.
#
# {html}
#
# ====================================================
# TASK
# ====================================================
#
# Find the SAME element that the failed locator was
# trying to identify.
#
# Prefer stable locators.
#
# Priority:
#
# 1. id
# 2. name
# 3. data-qa
# 4. data-testid
# 5. aria-label
# 6. css
# 7. xpath
#
# Never invent attributes.
#
# Never guess.
#
# Never explain.
#
# Never return markdown.
#
# Never return JSON.
#
# Return ONLY ONE locator.
#
# Examples
#
# id=submit
#
# name=pay-button
#
# css=#submit
#
# xpath=//button[@id='submit']
# """

"""
Enterprise Prompt Builder

Builds deterministic prompts for Ollama/Llama.

Goal:
Return ONLY one Selenium locator.
"""


class PromptBuilder:

    @staticmethod
    def build_locator_prompt(
            locator,
            page_title,
            page_url,
            html
    ):

        by, value = locator

        prompt = f"""
You are a Selenium Locator Recovery Engine.

Your ONLY job is to recover ONE broken Selenium locator.

====================================================
PAGE INFORMATION
====================================================

Title:
{page_title}

URL:
{page_url}

====================================================
FAILED LOCATOR
====================================================

{by}={value}

====================================================
AVAILABLE HTML
====================================================

Use ONLY the HTML below.

{html}

====================================================
RULES
====================================================

1. Find the SAME element the failed locator refers to.

2. Use ONLY attributes present in the supplied HTML.

3. NEVER invent attributes.

4. NEVER guess.

5. NEVER explain.

6. NEVER apologize.

7. NEVER output markdown.

8. NEVER output JSON.

9. NEVER output code blocks.

10. Output EXACTLY ONE locator.

====================================================
Locator priority
====================================================

1. id
2. name
3. data-qa
4. data-testid
5. aria-label
6. css
7. xpath

====================================================
VALID OUTPUT EXAMPLES
====================================================

id=submit

name=pay-button

css=#submit

xpath=//button[@id='submit']

====================================================
INVALID OUTPUT EXAMPLES
====================================================

The correct locator is id=submit

I recommend id=submit

Here is the locator:

id=submit

Thank you.
"""
        print("Prompt length =", len(prompt))
        print(prompt[:500])
        return prompt
