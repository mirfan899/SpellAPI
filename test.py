import requests
url = "http://127.0.0.1:5000/api/v1/spell"
payload = {'sentence': 'sodium attraction dorce'}
headers = {}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)


url = "http://127.0.0.1:5000/api/v1/split"
payload={'text': """James Smith was born on November 20, 1972 at St. Mary\'s Keller Memorial Hospital in Scranton, Pennsylvania.
James studied engineering and mathematics at Harvard university in 1990.
James bought 2 dogs, 3 computers, fur jacket, multiple diamonds while shopping in Seattle.
John Travolta bought 13 goldfish, 2 eels, 200 apples, and 4 parrots."""}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
