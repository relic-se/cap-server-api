# SPDX-FileCopyrightText: Copyright (c) 2026 Cooper Dalrymple (@relic-se)
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
`cap_api`
================================================================================

Python wrapper for Cap CAPTCHA server API

* Author(s): Cooper Dalrymple
"""

import json
from http.client import HTTPSConnection


class Server:
    """Establish server API connection to Cap instance."""

    def __init__(
        self,
        instance: str,
        api_key: str,
    ):
        """Create the server API connection.

        :param instance: The domain of the Cap server.
        :param api_key: The API key to connect to the server. Must be generated within Cap
            dashboard.
        """
        self._instance = instance
        self._api_key = api_key

    def _make_connection(self) -> HTTPSConnection:
        return HTTPSConnection(
            self._instance,
            port=443,
            timeout=10,
        )

    def _get(self, path: str, method: str = "GET") -> dict | list:
        response = None
        conn = self._make_connection()
        try:
            conn.request(
                method,
                path,
                headers={
                    "Authorization": f"Bot {self._api_key}",
                    "Accept": "application/json",
                },
            )
            response = json.loads(conn.getresponse().read())
        except Exception as e:
            print(f"Request failed: {e}")
            raise e
        finally:
            conn.close()
        return response

    def _post(self, path: str, data: dict | None = None) -> dict | list:
        headers = {
            "Authorization": f"Bot {self._api_key}",
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
            print(f"Request failed: {e}")
            raise e
        finally:
            conn.close()
        return response

    @property
    def about(self) -> dict:
        """Get basic information from the server. Returns a dict with the keys "bun", "ver" and
        "demo".
        """
        return self._get("/server/about")

    @property
    def keys(self) -> list:
        """Get a list of all keys on the Cap server. See :func:`get_key` for data format."""
        return self._get("/server/keys")

    def add_key(
        self,
        name: str,
        instrumentation: bool = True,
        blockAutomatedBrowsers: bool = True,
        corsOrigins: list | None = None,
    ) -> dict:
        """Create a new key. Returns a dict with the same keys as :func:`get_key` but also includes
        "secretKey".

        :param name: The name of the key.
        :param instrumentation: Whether or not you would like to enable instrumentation challenges.
        :param blockAutomatedBrowsers: Whether or not to attempt to block headless browsers.
        :param corsOrigins: Only these origins will be able to request challenges for this key.
        """
        data = {
            "name": name,
            "instrumentation": instrumentation,
            "blockAutomatedBrowsers": blockAutomatedBrowsers,
        }
        if corsOrigins is not None:
            data["corsOrigins"] = corsOrigins
        return self._post("/server/keys", data=data)

    def get_key(self, siteKey: str) -> dict:
        """Get information about a specific key by its "siteKey" value. Returns a dict with the keys
        "siteKey", "name", "created", "solvesLast24h" and "difference".

        :param siteKey: The site key of the key.
        """
        return self._get(f"/server/keys/{siteKey}")

    def delete_key(self, siteKey: str) -> dict:
        """Delete a key by its "siteKey" value.

        :param siteKey: The site key of the key.
        """
        return self._get(f"/server/keys/{siteKey}", method="DELETE")

    def rotate_secret(self, siteKey: str) -> dict:
        """Generate a new secret key for a key by its "siteKey" value. Returns a dict with the key
        "secretKey".

        :param siteKey: The site key of the key.
        """
        return self._post(f"/server/keys/{siteKey}/rotate-secret")
