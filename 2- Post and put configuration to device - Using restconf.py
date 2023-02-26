#Sending configuration to device with Restconf
 
import requests
import json
from rich import print as rprint

requests.packages.urllib3.disable_warnings()

#device access information
HOST = "192.168.200.200"
PORT = "443"
USER = "iman"
PASSWORD = "iman"

headers = {
      "Accept" : "application/yang-data+json", 
      "Content-Type" : "application/yang-data+json", 
   }

module1 = "ietf-interfaces:interfaces"
module2 = "Cisco-IOS-XE-native:native/router/router-ospf/ospf"
url = f"https://{HOST}:{PORT}/restconf/data/{module2}"

payload = {
        'interface': [
            {
                'name': 'Loopback113',
                'type': 'iana-if-type:softwareLoopback',
                'enabled': True,
                'ietf-ip:ipv4': {'address': [{'ip': '192.168.113.113', 'netmask': '255.255.255.255'}]},
                'ietf-ip:ipv6': {}
            }
        ]
}

payload_for_post = {
        'process-id': [
            {
                'id': 1,
                'network': [
                    {'ip': '192.168.12.0', 'wildcard': '0.0.0.255', 'area': 0},
                    {'ip': '192.168.13.0', 'wildcard': '0.0.0.255', 'area': 1},
                    {'ip': '192.168.14.0', 'wildcard': '0.0.0.255', 'area': 1},
                    {'ip': '192.168.111.0', 'wildcard': '0.0.0.255', 'area': 0}
                ],
                'router-id': '1.1.1.1'
            }
        ]
}

payload_for_put = {
    'Cisco-IOS-XE-ospf:ospf': {
        'process-id': [
            {
                'id': 1,
                'network': [
                    {'ip': '192.168.12.0', 'wildcard': '0.0.0.255', 'area': 0},
                    {'ip': '192.168.13.0', 'wildcard': '0.0.0.255', 'area': 1},
                    {'ip': '192.168.14.0', 'wildcard': '0.0.0.255', 'area': 1},
                    {'ip': '192.168.111.0', 'wildcard': '0.0.0.255', 'area': 0}
                ],
                'router-id': '11.11.11.11'
            }
        ]
    }
}

#using requeests.post for new config
#using requeests.put for replace config

#response = requests.post(url, headers=headers, data=json.dumps(payload1), auth=(USER, PASSWORD), verify=False)
response = requests.put(url, headers=headers, data=json.dumps(payload2), auth=(USER, PASSWORD), verify=False)



rprint(response)

