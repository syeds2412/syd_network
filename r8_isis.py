#Importing correct modules
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import SSHException
import os

#Cisco device to login
iosv_l3 = {'device_type': 'cisco_ios', 'ip': '192.168.1.18', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'}

#Below script shows ssh to the device and provide error in case error happens
#try:
net_connect = ConnectHandler(**iosv_l3)

#except NetMikoTimeoutException:
#	print('Device not reachable')
#	continue

#except NetMikoAuthenticationException:
#   print('Authentication failure')
#   continue

#except SSHException:
#    print('Make sure SSH is enabled.')
#    continue

#Will check if need for enable mode on Cisco ios 
if not net_connect.check_enable_mode():
	net_connect.enable()

#Lines to config on device
with open('r8_isis.txt') as f:
	lines = f.read().splitlines()

print(lines)

#Push required config to the device
output = net_connect.send_config_set(lines)

print(output)

