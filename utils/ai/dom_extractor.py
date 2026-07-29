from bs4 import BeautifulSoup, Comment
import re


class DOMExtractor:

    WINDOW = 4

    @staticmethod
    def extract(driver, failed_locator=None):

        html = driver.page_source

        soup = BeautifulSoup(html, "html.parser")

        #
        # Remove noisy tags
        #

        for tag in soup([
            "script",
            "style",
            "svg",
            "path",
            "iframe",
            "meta",
            "link",
            "noscript"
        ]):
            tag.decompose()

        #
        # Remove comments
        #

        for comment in soup.find_all(
                string=lambda t: isinstance(t, Comment)
        ):
            comment.extract()

        #
        # No failed locator?
        #

        if failed_locator is None:
            return str(soup)

        locator_type, locator_value = failed_locator

        #
        # Build search tokens
        #

        tokens = DOMExtractor._build_tokens(locator_type, locator_value)

        #
        # Collect candidate elements
        #

        candidates = []

        important = soup.find_all([
            "button",
            "a",
            "input",
            "label",
            "select",
            "textarea",
            "form",
            "option",
            "h1",
            "h2",
            "h3"
        ])

        for tag in important:

            text = tag.get_text(" ", strip=True).lower()

            attrs = " ".join(

                str(v)

                for v in tag.attrs.values()

            ).lower()

            searchable = text + " " + attrs

            score = 0

            for token in tokens:

                if token in searchable:
                    score += 1

            if score:
                candidates.append((score, tag))

        #
        # Nothing matched
        #

        if not candidates:

            return "\n".join(
                str(x)
                for x in important[:25]
            )

        #
        # Best matches first
        #

        candidates.sort(
            key=lambda x: x[0],
            reverse=True
        )

        selected = []

        for _, tag in candidates[:10]:

            selected.append(str(tag))

            #
            # Parent helps AI
            #

            if tag.parent:

                selected.append(str(tag.parent))

        #
        # Remove duplicates
        #

        unique = []

        seen = set()

        for html in selected:

            if html not in seen:

                unique.append(html)

                seen.add(html)

        return "\n\n".join(unique)

    # --------------------------------------------------------

    @staticmethod
    def _build_tokens(locator_type, locator_value):

        tokens = []

        value = locator_value.lower()

        #
        # xpath text()
        #

        m = re.findall(
            r"text\(\)\s*=\s*['\"]([^'\"]+)['\"]",
            value
        )

        tokens.extend(m)

        #
        # normalize-space()
        #

        m = re.findall(
            r"normalize-space\(text\(\)\)\s*=\s*['\"]([^'\"]+)['\"]",
            value
        )

        tokens.extend(m)

        #
        # id=
        #

        m = re.findall(
            r"@id=['\"]([^'\"]+)['\"]",
            value
        )

        tokens.extend(m)

        #
        # name=
        #

        m = re.findall(
            r"@name=['\"]([^'\"]+)['\"]",
            value
        )

        tokens.extend(m)

        #
        # CSS
        #

        if locator_type == "css selector":

            tokens.extend(

                re.findall(
                    r"[A-Za-z0-9_-]+",
                    locator_value
                )

            )

        #
        # id locator
        #

        if locator_type == "id":

            tokens.append(locator_value.lower())

        #
        # name locator
        #

        if locator_type == "name":

            tokens.append(locator_value.lower())

        return list(set(tokens))