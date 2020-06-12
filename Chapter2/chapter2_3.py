#!/usr/bin/env python


from username import username,password
import paramiko, time, json

with open('devices.json', 'r') as f:
    devices = json.load(f)

with open('commands.txt' , 'r') as f:
    commands = f.readlines()

max_buffer = 65535

for device in devices.keys():
    outputFilename = device + '_output.txt'
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'],username=username, password=password, look_for_keys=False, allow_agent=False)
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    with open(outputFilename, 'wb') as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(2)
            output = new_connection.recv(max_buffer)
            print(output)
            f.write(output)
