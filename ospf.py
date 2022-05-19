#!/usr/bin/env python3

from netmiko import ConnectHandler

iosv_l3 = {'device_type': 'cisco_ios', 'ip': '10.10.10.1', 'username': 'cisco', 'password': 'cisco'}

with open('ospf') as f:
    lines = f.read().splitlines()

print(lines)

net_connect = ConnectHandler(**iosv_l3)
output = net_connect.send_config_set(lines)

print(output)

