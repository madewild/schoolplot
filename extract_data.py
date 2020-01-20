"""Extracting school adresses and shapefile"""

from io import BytesIO
import requests
from zipfile import ZipFile

shapezip = "https://www.eea.europa.eu/data-and-maps/data/eea-reference-grids-2/gis-files/belgium-shapefile/at_download/file"
r = requests.get(shapezip, allow_redirects=True)
with ZipFile(BytesIO(r.content), 'r') as zipdata:
    zipdata.extractall
