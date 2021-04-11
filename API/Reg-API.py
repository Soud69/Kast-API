import requests
# Importing requests 
username = input("Username: ")
# Username Input
email = input("Email: ")
# Email Input
password = input("Password: ")
# Password Input

url = "https://api-auth.evasyst.com/api/register"
# Reg API URL

data = {
	"email": email,
	"login": username,
	"password": password
	}
# Reg API Data

headers = {
	"Host": "api-auth.evasyst.com",
	"Content-Type": "application/json",
	"Accept": "*/*",
	"Accept-Encoding": "gzip, deflate, br",
	"Connection": "keep-alive",
	"App-Device": "iphone",
	"App-OS": "ios",
	"User-Agent": "Kast/1.8.2 (iPhone; iOS 14.2.1; Scale/3.00)",
	"Accept-Language": "en-US;q=1, ar-US;q=0.9",
	"App-Version": "1.8.2",
	"App-Build": 142
	} 
# Reg API Headers

req = requests.post(url, json=data, headers=headers)
# Reg API Request

if "Incorrect password length" in req.text:
	print("Short Password, Try Again")
	# Short Password 

elif "Login is empty" in req.text:
	print("Login Info Is Empty, Try Again")
	# Empty Login Info
	
elif f'login":"{username}' in req.text:
	print("Reg Success")
	# Reg Success

elif "Login already exists" in req.text:
	print("Username Already In Use, Try Again")
	# Username Used

elif "Login must not contain special characters" in req.text:
	print("Special Charecters Not Allowed, Try Again")	
	# Charecters (.*?=+) Not Allowed

elif "Email already exists" in req.text:
	print("Email Already In Use, Try Again")
	# Used Email

else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
