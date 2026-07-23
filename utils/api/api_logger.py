"""
Enterprise API Logger
"""

import json
import logging
import time

from reports.api.api_reporter import ApiReporter


class ApiLogger:

    logger = logging.getLogger("API")

    # -------------------------------------------------------------

    @classmethod
    def log_request(

            cls,

            method,

            url,

            payload=None,

            headers=None

    ):

        start = time.perf_counter()

        cls.logger.info("=" * 80)

        cls.logger.info("API REQUEST")

        cls.logger.info("Method : %s", method)

        cls.logger.info("URL    : %s", url)

        if headers:

            cls.logger.info(

                "Headers:\n%s",

                json.dumps(

                    headers,

                    indent=4

                )

            )

        if payload:

            cls.logger.info(

                "Payload:\n%s",

                json.dumps(

                    payload,

                    indent=4,

                    default=str

                )

            )

        return start

    # -------------------------------------------------------------

    @classmethod
    def log_response(

            cls,

            method,

            url,

            request,

            response,

            start_time

    ):

        duration = (

            time.perf_counter()

            - start_time

        ) * 1000

        cls.logger.info("-" * 80)

        cls.logger.info(

            "Status Code : %s",

            response.status_code

        )

        cls.logger.info(

            "Duration    : %.2f ms",

            duration

        )

        cls.logger.info(

            "Response Size : %.2f KB",

            len(

                response.text.encode()

            ) / 1024

        )

        cls.logger.info(

            "Response:\n%s",

            response.text

        )

        cls.logger.info("=" * 80)

        #
        # Save Report
        #

        ApiReporter.save_transaction(

            method=method,

            url=url,

            request=request,

            response=response.text,

            status=response.status_code,

            duration=duration

        )