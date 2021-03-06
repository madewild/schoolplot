"""Retrieve geocoordinates with Google Geocoding"""

import os
import sys
import pandas as pd
import requests
import json

degree = sys.argv[1]

api_key = os.getenv("GCLOUD_API_KEY")

output = open(f"data/{degree}_coordinates.tsv", "w")
header = "name\tlat\tlong\n"
output.write(header)

df = pd.read_csv(f"data/{degree}_addresses.tsv", sep="\t")
for i, school in enumerate(df["name"]):
    address = df["address"][i]
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    r = requests.get(url)
    json_code = json.loads(r.content)["results"]
    if json_code:
        lat = json_code[0]["geometry"]["location"]["lat"]
        lon = json_code[0]["geometry"]["location"]["lng"]
        output_string = f"{school}\t{lat}\t{lon}\n"
        output.write(output_string)
    else:
        print(address)
