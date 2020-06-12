# !/usr/bin/env python3

import ncclient
from ncclient import manager


conn = manager.connect(
        host='172.16.0.165',
        port=22,
        username='admin',
        password='@dmin123',
        hostkey_verify=False,
        device_params={'name': 'nexus'},
        look_for_keys=False
        )

for value in conn.server_capabilities:
    print(value)
    conn.close_session()
