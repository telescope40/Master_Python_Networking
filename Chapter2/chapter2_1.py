#!/usr/bin/env python
import pexpect

devices = {'R1':{'prompt': 'R1#', 'ip':'172.16.0.199'},
          'R2': {'prompt': 'R2#', 'ip': '172.16.0.169'}}

username = 'admin'
password = 'admin'

for device in devices.keys():
    device_prompt = devices[device]['prompt']
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt)
    child.sendline('show version | i V')
    child.expect(device_prompt)
    print(child.before)
    child.sendline('exit')
