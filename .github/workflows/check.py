#!/usr/bin/env python
import sys
import time
from pyzabbix import ZabbixAPI

for x in range(20):
    try:
        zapi = ZabbixAPI(url="http://localhost:8050/")
        zapi.login("Admin","zabbix")
    except:
        print('Zabbix 5.0 API is not ready...')
        time.sleep(5)
    else:
        zapi.do_request('user.logout')
        break;
else:
  sys.exit('Failed to wait for Zabbix API to be ready')
  
for x in range(20):
    try:
        zapi = ZabbixAPI(url="http://localhost:8054/")
        zapi.login("Admin","zabbix")
    except:
        print('Zabbix 5.4 API is not ready...')
        time.sleep(5)
    else:
        zapi.do_request('user.logout')
        break;
else:
  sys.exit('Failed to wait for Zabbix API to be ready')

for x in range(20):
    try:
        zapi = ZabbixAPI(url="http://localhost:8060/")
        zapi.login("Admin","zabbix")
    except:
        print('Zabbix 6.0 API is not ready...')
        time.sleep(5)
    else:
        zapi.do_request('user.logout')
        break;
else:
  sys.exit('Failed to wait for Zabbix API to be ready')

for x in range(20):
    try:
        zapi = ZabbixAPI(url="http://localhost:8064/")
        zapi.login("Admin","zabbix")
    except:
        print('Zabbix 6.4 API is not ready...')
        time.sleep(5)
    else:
        zapi.do_request('user.logout')
        break;
else:
  sys.exit('Failed to wait for Zabbix API to be ready')