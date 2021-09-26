import requests

requests.packages.urllib3.disable_warnings()
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
auth_url = "https://sandbox-sdwan-1.cisco.com/j_security_check"
credentials = {"j_username": "devnetuser", "j_password": "RG!_Yw919_83"}
session = requests.session()



response = session.post(auth_url, headers=HEADERS, data=credentials, verify=False)
url = "https://sandbox-sdwan-1.cisco.com/dataservice/device"
response = session.get(url, verify=False)

session_cookies = session.cookies
session.get(url, verify=False)
cookies_dictionary = session_cookies.get_dict()
print(cookies_dictionary)

token_url = "https://sandbox-sdwan-1.cisco.com/dataservice/client/token"
HEADERS = {"Content-Type": "application/json"}
response2 = session.get(token_url, headers=HEADERS, verify=False)
session_token=response2.content
print(session_token)
