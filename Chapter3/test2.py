"""
NX-API-BOT 
"""
import requests
import json

"""
Modify these please
"""

url='http://172.16.0.165/ins'
switchuser='admin'
switchpassword='@dmin123'

myheaders={'content-type':'application/json-rpc'}
payload=[
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "show version",
            "version": 1.2
                    },
                    "id": 1
             }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
