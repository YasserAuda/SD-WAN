import requests
import tabulate
import json

requests.packages.urllib3.disable_warnings()
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
auth_url = "https://sandbox-sdwan-1.cisco.com/j_security_check"
credentials = {"j_username": "devnetuser", "j_password": "RG!_Yw919_83"}
session = requests.session()
response = session.post(auth_url, headers=HEADERS, data=credentials, verify=False)
url = "https://sandbox-sdwan-1.cisco.com/dataservice/device"
response = session.get(url, verify=False)
json_response = json.loads(response.text)
items = json_response['data']
headers = ["Host-Name", "Device Type", "Device ID", "System IP", "Site ID", "Version" , "Device Model" ]
table = []
for item in items:
   tr = [ item ["host-name"], item["device-type"], item["uuid"], item["system-ip"], item["site-id"], item["version"] , item["device-model"] ]
   table.append(tr)
print(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))

'''
Try it: https://devasc-sdwan-1.cisco.com/apidocs/
Log in using username devnetuser and password RE!_Yw519_27
'''
#https://github.com/YasserAuda/SD-WAN/
