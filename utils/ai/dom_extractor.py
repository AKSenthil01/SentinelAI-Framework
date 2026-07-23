class DOMExtractor:

    MAX_HTML = 25000      # start with 25 KB

    @staticmethod
    def extract(driver, locator):

        script = """
        let nodes = document.querySelectorAll(
            "button,input,a,form,select"
        );

        let html="";

        nodes.forEach(n=>{
            html += n.outerHTML + "\\n";
        });

        return html;
        """

        html = driver.execute_script(script)

        print("\nDOM SIZE =", len(html))

        if len(html) > DOMExtractor.MAX_HTML:
            html = html[:DOMExtractor.MAX_HTML]

        return html