import requests
import json


api_key = ""
date = "21-12-2019" #dd-mm-yyyy
src = "adi"
dest = "brc"
url = "https://api.railwayapi.com/v2/between/source/{}/dest/{}/date/{}/apikey/{}/".format(src, dest, date, api_key)
responses = requests.get(url)

print(responses.json())
