import requests

url = "https://opensea.io/assets/0x1eff5ed809c994ee2f500f076cef22ef3fd9c25d/8"

response = requests.request("GET", url)

print(response.text)
