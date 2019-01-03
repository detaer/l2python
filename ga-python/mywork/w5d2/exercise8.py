#%%
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# Decode the raw JSON data.
response_data = response.json()

print(response_data['name'])
print(response_data['username'])
print(response_data['email'])
print(response_data['phone'])