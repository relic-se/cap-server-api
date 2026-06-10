# SPDX-FileCopyrightText: Copyright (c) 2026 Cooper Dalrymple (@relic-se)
#
# SPDX-License-Identifier: GPL-3.0-or-later

from cap_api import Server
from secrets import INSTANCE, API_KEY  # Provide instance host and API key for Cap server within secrets.py

KEY_NAME = "simpletest"

# Begin server connection
server = Server(INSTANCE, API_KEY)

# Read server info (version, etc)
print(server.about())

# Create new key if not found or rotate secret of existing key
key = next(iter(filter(lambda x: x["name"] == KEY_NAME, server.keys)))
if key is not None:
    key["secretKey"] = server.rotate_secret(key["siteKey"])["secretKey"]
else:
    key = server.add_key(KEY_NAME)
print(key)
