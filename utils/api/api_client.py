"""
Enterprise API Client

Features

✓ Base URL
✓ Session Reuse
✓ Logging
✓ Timeout
✓ SSL Handling
✓ GET
✓ POST
✓ PUT
✓ DELETE
"""

import requests

from utils.api.api_config import (
    BASE_API_URL,
    DEFAULT_TIMEOUT,
    VERIFY_SSL
)

from utils.api.api_logger import ApiLogger


class ApiClient:

    session = requests.Session()

    # ---------------------------------------------------------

    @classmethod
    def get(

            cls,

            endpoint,

            headers=None,

            params=None

    ):

        url = BASE_API_URL + endpoint

        start = ApiLogger.log_request(

            method="GET",

            url=url,

            headers=headers,

            payload=params

        )

        response = cls.session.get(

            url,

            headers=headers,

            params=params,

            timeout=DEFAULT_TIMEOUT,

            verify=VERIFY_SSL

        )

        ApiLogger.log_response(

            method="GET",

            url=url,

            request=params,

            response=response,

            start_time=start

        )

        return response

    # ---------------------------------------------------------

    @classmethod
    def post(

            cls,

            endpoint,

            headers=None,

            payload=None,

            data=None

    ):

        url = BASE_API_URL + endpoint

        start = ApiLogger.log_request(

            method="POST",

            url=url,

            headers=headers,

            payload=payload if payload else data

        )

        response = cls.session.post(

            url,

            headers=headers,

            json=payload,

            data=data,

            timeout=DEFAULT_TIMEOUT,

            verify=VERIFY_SSL

        )

        ApiLogger.log_response(

            method="POST",

            url=url,

            request=payload if payload else data,

            response=response,

            start_time=start

        )
        return response

    # ---------------------------------------------------------

    @classmethod
    def put(

            cls,

            endpoint,

            headers=None,

            payload=None,

            data=None

    ):

        url = BASE_API_URL + endpoint

        start = ApiLogger.log_request(

            method="PUT",

            url=url,

            headers=headers,

            payload=payload if payload else data

        )

        response = cls.session.put(

            url,

            headers=headers,

            json=payload,

            data=data,

            timeout=DEFAULT_TIMEOUT,

            verify=VERIFY_SSL

        )

        ApiLogger.log_response(

            method="PUT",

            url=url,

            request=payload if payload else data,

            response=response,

            start_time=start

        )
        return response

    # ---------------------------------------------------------

    @classmethod
    def delete(

            cls,

            endpoint,

            headers=None,

            payload=None,

            data=None

    ):

        url = BASE_API_URL + endpoint

        start = ApiLogger.log_request(

            method="DELETE",

            url=url,

            headers=headers,

            payload=payload if payload else data

        )

        response = cls.session.delete(

            url,

            headers=headers,

            json=payload,

            data=data,

            timeout=DEFAULT_TIMEOUT,

            verify=VERIFY_SSL

        )

        ApiLogger.log_response(

            method="DELETE",

            url=url,

            request=payload if payload else data,

            response=response,

            start_time=start

        )
        return response