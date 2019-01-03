#%%
import requests

response = requests.get("http://api.open-notify.org/astros.json")

# Decode the raw JSON data.
response_data = response.json()

print(response_data)
for person in response_data['people']:
    print(person['name'])

for person in response_data['people']:
    if person['name'] == 'Sergey Prokopyev':
        print(person['craft'])