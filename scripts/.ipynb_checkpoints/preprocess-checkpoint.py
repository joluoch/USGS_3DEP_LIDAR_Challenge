import warnings
warnings.filterwarnings('ignore')
# import geoplot as gplt

import geopandas as gpd
# import geoplot.crs as gcrs
import imageio
import pandas as pd
import pathlib
import matplotlib.pyplot as plt
import plotly.offline as go_offline
import plotly.graph_objects as go
from shapely.geometry import Point
import mapclassify as mc
import numpy as np
import laspy
import rasterio
from rasterio import mask
import folium


def geometry (csvpath): 
    
    print ('===================READING CSV  =====================')
    pan = pd.read_csv(csvpath)
    
    geo = pan[["X","Y","Z"]]
    
    #convert xyz to geodataframe
    geometry = [Point(xy) for xy in zip(pd.to_numeric(gp['X']), pd.to_numeric(gp['Y']))]
    gdf = gpd.GeoDataFrame(gp, crs='epsg:4326',geometry=geometry)
    gdf = gdf[["Z", "geometry"]]
    gdf = gdf.rename(columns={"Z": "elevation_m", "geometry": "geometry"})
    #gdf.head()
    
    return gdf

