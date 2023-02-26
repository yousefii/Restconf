#delete configuraion with restconf

import requests
import json
from rich import print as rprint

requests.packages.urllib3.disable_warnings()

#Access device information
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
module3 = "Cisco-IOS-XE-native:native"




url1 = f"https://{HOST}:{PORT}/restconf/data/{module2}/process-id=1"

response = requests.delete(url=url1, headers=headers, auth=(USER, PASSWORD), verify=False)

rprint(response)


