#%%
import requests

rawgiffydata = requests.get('http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC')

print(giffydata)

giffydata = rawgiffydata.xml()