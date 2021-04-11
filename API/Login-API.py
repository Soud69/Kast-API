import requests
import json
# Importing json And requests 

url = "https://api-auth.evasyst.com/api/login"
# Login API URL

headers = {
	"Host": "api-auth.evasyst.com",
	"Accept": "*/*",
	"Authorization": "",
	"App-Version": "1.8.2",
	"App-OS": "ios",
	"App-Device": "iphone",
	"Accept-Language": "en-US;q=1, ar-US;q=0.9",
	"Accept-Encoding": "gzip, deflate, br",
	"Content-Type": "application/json",
	"User-Agent": "Kast/1.8.2 (iPhone; iOS 14.2.1; Scale/3.00)",
	"Connection": "keep-alive",
	"App-Build": 142
	} 
# Login API Headers

email = input("Username/Email: ") 
# Email Or Username Input
password = input("Password: ") 
# Password Input

data = {
	"login": email,
	"password": password,
	"rememberMe": "true"
}
# Login API Data

req = requests.post(url, json=data, headers=headers)
# Login API Request
if "was not activated" in req.text:
	print("Account Not Activated, Try Again")
	# Account Not Activated

elif "PARAMETER_MISSING" in req.text:
	print("Missing Something, Try Again")
	# Missing Data

elif "Bad credentials" in req.text:
	print("Login Failed, Try Again")
	# Wrong Login Info

elif "id_token" in req.text:
	print("Login Success")
	token = json.loads(req.text)["id_token"]
	# Login Success And Parse Login Token

else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
