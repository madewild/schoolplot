"""Plotting geocoordinates on a map with GeoPandas"""

import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon



be_map = gpd.read_file("/home/max/belgium_shapefile/be_1km.shp")
fig, ax = plt.subplots(figsize = (100,100))
be_map.plot(ax=ax)
plt.title("Belgium")
plt.show()
#plt.savefig('./schools.jpg')
