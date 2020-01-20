"""Retrieve geocoordinates with OSM Nominatim API"""

import os
import pandas as pd
import requests
import json

api_key = os.getenv("GCLOUD_API_KEY")

output = open("data/coordinates.tsv", "w")
header = "name\tlat\tlong\n"
output.write(header)

df = pd.read_csv("data/schools.tsv", sep="\t")
for i, school in enumerate(df["name"]):
    address = df["address"][i]
    #url = f"https://nominatim.openstreetmap.org/search.php?format=json&q={address}"
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={school}, {address}&key={api_key}"
    r = requests.get(url)
    json_code = json.loads(r.content)["results"]
    if json_code:
        #lat = json_code[0]["lat"]
        lat = json_code[0]["geometry"]["location"]["lat"]
        #lon = json_code[0]["lon"]
        lon = json_code[0]["geometry"]["location"]["lng"]
        output_string = f"{school}\t{lat}\t{lon}\n"
        output.write(output_string)
    else:
        print(address)