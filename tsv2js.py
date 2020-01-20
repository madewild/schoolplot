"""Convert TSV data to Leaflet format"""

import pandas as pd

output = open("schools.txt", "w")
df = pd.read_csv("ecoles.tsv", sep="\t")
for i, school in enumerate(df["name"]):
    lat = df["lat"][i]
    lon = df["long"][i]
    string = f'            L.marker([{lat}, {lon}]).addTo(mymap)\n'
    string += f'                .bindPopup("{school}")\n'
    output.write(string)
output.close()
