"""Convert TSV data to Leaflet format"""

import pandas as pd

output = open("schools.html", "w")
header = """<html>
    <head>
        <title>Écoles</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
        <link rel="stylesheet" href="style.css"/>
        <script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"
   integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew=="
   crossorigin=""></script>
    </head>
    <body>
        <div id="mapid"></div>
        <script>
            var mymap = L.map('mapid').setView([50.4525, 3.945], 10);

            L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
                maxZoom: 18,
                id: 'mapbox/streets-v11'
            }).addTo(mymap);

"""
output.write(header)

df = pd.read_csv("data/coordinates.tsv", sep="\t")
df2 = pd.read_csv("data/addresses.tsv", sep="\t")
for i, school in enumerate(df["name"]):
    lat = df["lat"][i]
    lon = df["long"][i]
    address = df2["address"][i]
    address = address.replace(", Belgium", "")
    string = f'            L.marker([{lat}, {lon}]).addTo(mymap)\n'
    string += f'                .bindPopup("<b>{school}</b><br/>{address}")\n'
    output.write(string)

footer = """
        </script>
    </body>
</html>"""
output.write(footer)
output.close()
