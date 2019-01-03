#%%
import geocoder
import requests

dark_sky_api_key_location = open('/Users/detaer/.dark_sky_api.key', 'r')
dark_sky_key = dark_sky_api_key_location.read().rstrip()
dark_sky_api_key_location.close()

# print(dark_sky_key)
API_URL = f"https://api.darksky.net/forecast/{dark_sky_key}/"

print(API_URL)

#places we want to go
destinations = [
    "Space Needle",
    "Crater Lake",
    "Golden Gate Bridge",
    "Yosemite National Park",
    "Las Vegas, Nevada",
    "Grand Canyon National Park",
    "Aspen, Colorado",
    "Mount Rushmore",
    "Yellowstone National Park",
    "Sandpoint, Idaho",
    "Banff National Park",
    "Capilano Suspension Bridge"
    ]

# loop through the list
for place in destinations:
    #geolocation for each
    get_location = geocoder.arcgis(place)
    lat, long = round(get_location.latlng[0],4), round(get_location.latlng[1],4)
    print(f"{place}, is at ({lat}, {long})")
    # complete_api_url 

