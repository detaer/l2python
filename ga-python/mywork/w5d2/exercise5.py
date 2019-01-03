#%%
import requests

response = requests.get("https://api.github.com/events")


response_data = response.json()
print(response_data[0]['id'])