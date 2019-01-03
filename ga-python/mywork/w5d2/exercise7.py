#%%
import requests

blargl = requests.get('http://api.giphy.com/v1/gifs/search?q=bananna')

bananna = blargl.xml()
print(bananna)