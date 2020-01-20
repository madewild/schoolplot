"""Retrieve geocoordinates with OSM Nominatim API"""

import pandas as pd
import requests
import json

output = open("coordinates.tsv", "w")
header = "name\tlat\tlong\n"
output.write(header)

df = pd.read_csv("schools.tsv", sep="\t")
for i, school in enumerate(df["name"]):
    address = df["address"][i]
    url = f"https://nominatim.openstreetmap.org/search.php?format=json&q={address}"
    r = requests.get(url)
    json_code = json.loads(r.content)
    if json_code:
        lat = json_code[0]["lat"]
        lon = json_code[0]["lon"]
        output_string = f"{school}\t{lat}\t{lon}\n"
        output.write(output_string)
    else:
        print(address)