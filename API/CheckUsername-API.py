import requests
# Importing requests 

username = input("Username: ")
# Username Input

url = f"https://api-auth.evasyst.com/api/checklogin/{username}"
# Check API URL

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
# Check API Headers

req = requests.get(url, headers=headers)

# Check API Request

if 'exists":true' in req.text:
	print("Username Taken, Try Again")
	# Taken Username

elif 'exists":false' in req.text:
	print("Username Available")
	# Found Username

else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
