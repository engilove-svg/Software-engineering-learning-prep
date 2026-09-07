import requests

response = requests.get("https://example.com")

print(response.status_code)


#requests
   #↓
#sent a request to example.com
   #↓
#website responded
  # ↓
#response.status_code
 #  ↓
#200
