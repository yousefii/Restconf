#Getting configuration from device - using restconf

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
url = f"https://{HOST}:{PORT}/restconf/data/{module1}"


response = requests.get(url, headers=headers, auth=(USER, PASSWORD), verify=False).json()



rprint(response)
