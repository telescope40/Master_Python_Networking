#!/usr/bin/env python3

import requests
import json


url='http://172.16.0.165/ins'
switchuser='admin'
switchpassword='@dmin123'

myheaders={'content-type':'application/json-rpc'}
payload=[
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "interface ethernet 2/1",
            "version": 1.2
                    },
                    "id": 1
             },
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
            "cmd": "description foo-bar",
            "version": 1.2
                    },
                    "id": 1
              },
    
    ]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
print(response)
