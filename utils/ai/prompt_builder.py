# """
# Enterprise Prompt Builder
#
# Builds deterministic prompts for Ollama.
#
# Goal:
# Return ONLY one Selenium locator for the REAL element.
# """
#
#
# class PromptBuilder:
#
#     @staticmethod
#     def build_locator_prompt(locator, page_title, page_url, html):
#
#         if locator is None:
#             raise ValueError("locator cannot be None")
#
#         if html is None:
#             raise ValueError("HTML extraction returned None")
#
#         by, value = locator
#
#         prompt = f"""
# You are an expert Selenium Locator Recovery Engine.
#
# Your ONLY task is to identify the REAL locator of the target element.
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
# BROKEN LOCATOR
# ====================================================
#
# The locator below is INVALID.
#
# DO NOT repair it.
#
# DO NOT rewrite it.
#
# DO NOT convert it to another locator strategy.
#
# DO NOT reuse its value.
#
# Ignore it completely.
#
# Broken locator:
#
# {by}={value}
#
# The recovered locator MUST NOT contain:
#
# {value}
#
# ====================================================
#
# TOP MATCHING DOM ELEMENTS
#
# ====================================================
#
# The elements below are already ranked by similarity.
#
# Recover ONLY using these candidates.
#
# If none represents the original element,
#
# return ONLY
#
# NOT_FOUND
#
# ====================================================
#
# {html}
#
# ====================================================
# YOUR TASK
# ====================================================
#
# Find the REAL HTML element that the broken locator
# was originally intended to identify.
#
# Recover the BEST Selenium locator for that element.
#
# ====================================================
# LOCATOR PRIORITY
# ====================================================
#
# 1. id
# 2. name
# 3. data-qa
# 4. data-testid
# 5. aria-label
# 6. css
# 7. xpath
#
# ====================================================
# STRICT RULES
# ====================================================
#
# 1. The HTML contains the correct element.
#
# 2. Recover ONLY that element.
#
# 3. Never choose another button.
#
# 4. Never choose another link.
#
# 5. Never return a locator for a different action.
#
# 6. If an id exists, always return the id.
#
# 7. Otherwise use data-qa.
#
# 8. Otherwise use name.
#
# 9. Only use CSS when none of the above exist.
#
# 10.Return exactly ONE locator.
#
# 11.Ignore the broken locator completely.
#
# 12. Never return the same locator value.
#
# 13. Never rewrite the broken locator.
#
# 14. Never convert the broken locator to CSS/XPath.
#
# 15. Never invent attributes.
#
# 16. Use ONLY attributes present in the HTML.
#
# 17. Prefer unique stable attributes.
#
# 18. Return EXACTLY ONE locator.
#
# 19. No explanation.
#
# 20. No markdown.
#
# 21. No JSON.
#
# 22. No code block.
#
# 23.If the element has BOTH an id and data-qa,always prefer id.
#
# ====================================================
# OUTPUT FORMAT
# ====================================================
#
# Return ONLY one line.
#
# Examples:
#
# id=submit
#
# name=checkout
#
# css=button.btn.btn-primary.submit-button
#
# xpath=//button[@id='submit']
# """
#
#         if not prompt.strip():
#             raise RuntimeError("Generated prompt is empty")
#
#         return prompt

class PromptBuilder:

    @staticmethod
    def build_locator_prompt(

            locator,

            page_title,

            page_url,

            html

    ):

        return f"""
You are an expert Selenium automation engineer.

Broken locator

{locator}

Page title

{page_title}

URL

{page_url}

Relevant DOM

{html}

Your task:

Find the BEST locator for the SAME element.

Priority:

1. id=
2. name=
3. css=
4. xpath=

Rules:

- Return ONLY ONE locator.
- Do NOT explain.
- Do NOT use markdown.
- Do NOT use bullets.
- Do NOT return JSON.
- Output must be exactly one line.

Examples

id=submit

name=email

css=.submit-button

xpath=//button[@id='submit']

=================================================

IMPORTANT

Return ONLY ONE locator.

Allowed format

id=submit

name=username

css=.submit-button

xpath=//button[@id='submit']

Do NOT explain.

Do NOT repeat the broken locator.

Do NOT write markdown.

Do NOT write paragraphs.

Output MUST contain ONLY ONE locator.

"""