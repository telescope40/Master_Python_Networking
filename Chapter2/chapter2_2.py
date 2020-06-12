#!/usr/bin/env python


from pexpect import pxssh
from username import username,password

devices = {'R1':{'prompt': 'R1#', 'ip':'172.16.0.199'},
            'R2': {'prompt': 'R2#', 'ip': '172.16.0.169'}}


commands = ['term length 0', 'show version' , 'show run']


for device in devices.keys():
    outputFilename = device + '_output.txt'
    device_prompt = devices[device]['prompt']
    child = pxssh.pxssh()
    child.login(devices[device]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)
    # Loop through commands

    with open(outputFilename, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt)
            f.write(child.before)
    child.logout()
