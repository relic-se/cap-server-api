# SPDX-FileCopyrightText: Copyright (c) 2026 Cooper Dalrymple (@relic-se)
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
`cap_api`
================================================================================

Python wrapper for Cap CAPTCHA server API

* Author(s): Cooper Dalrymple
"""

from http.client import HTTPSConnection
import json

class Server:
    """Establish server API connection to Cap instance."""

    def __init__(
        self,
        instance: str,
        api_key: str,
    ):
        """Create the server API connection.

        :param instance: The domain of the Cap server.
        :param api_key: The API key to connect to the server. Must be generated within Cap dashboard.
        """
        self._instance = instance
        self._api_key = api_key

    def _make_connection(self) -> HTTPSConnection:
        return HTTPSConnection(
            self._instance,
            port=443,
            timeout=10,
        )

    def _get(self, path: str, method: str = "GET") -> dict|list:
        response = None
        conn = self._make_connection()
        try:
            conn.request(
                method,
                path,
                headers={
                    "Authorization": "Bot {}".format(self._api_key),
                    "Accept": "application/json",
                },
            )
            response = json.loads(conn.getresponse().read())
        except Exception as e:
            print("Request failed: {}".format(e))
            raise e
        finally:
            conn.close()
        return response

    def _post(self, path: str, data: dict|None = None) -> dict|list:
        headers = {
            "Authorization": "Bot {}".format(self._api_key),
            "Accept": "application/json",
        }
        if data is not None:
            headers["Content-Type"] = "application/json"
        response = None
        conn = self._make_connection()
        try:
            conn.request(
                "POST",
                path,
                body=json.dumps(data) if data is not None else None,
                headers=headers,
            )
            response = json.loads(conn.getresponse().read())
        except Exception as e:
            print("Request failed: {}".format(e))
            raise e
        finally:
            conn.close()
        return response

    @property
    def about(self) -> dict:
        return self._get("/server/about")

    @property
    def keys(self) -> list:
        return self._get("/server/keys")

    def add_key(self, name: str, instrumentation: bool = True, blockAutomatedBrowsers: bool = True, corsOrigins: list|None = None) -> dict:
        data = {
            "name": name,
            "instrumentation": instrumentation,
            "blockAutomatedBrowsers": blockAutomatedBrowsers,
        }
        if corsOrigins is not None:
            data["corsOrigins"] = corsOrigins
        return self._post("/server/keys", data=data)

    def get_key(self, siteKey: str) -> dict:
        return self._get("/server/keys/{}".format(siteKey))
    
    def delete_key(self, siteKey: str) -> dict:
        return self._get("/server/keys/{}".format(siteKey), method="DELETE")

    def rotate_secret(self, siteKey: str) -> dict:
        return self._post("/server/keys/{}/rotate-secret".format(siteKey))
