import warnings
warnings.filterwarnings('ignore')
# import geoplot as gplt

import geopandas as gpd
# import geoplot.crs as gcrs
import imageio
import pandas as pd
import pathlib
import matplotlib.pyplot as plt
from shapely.geometry import Point
import mapclassify as mc
import numpy as np
import laspy
import rasterio
from rasterio import mask
import folium
import plotly.offline as go_offline
import plotly.graph_objects as go


## Plot raster/tif image
# --------------------
def plot_raster(tifile: str, title=''):
    """
    Plots raster tif image both in log scale(+1) and original verion
    """
    spr_tif = tifile
    raster_spr = rasterio.open(spr_tif)
    spr_data = raster_spr.read(1)
    fig, (axlog, axorg) = plt.subplots(1, 2, figsize=(14,7))
    im1 = axlog.imshow(np.log1p(spr_data)) # vmin=0, vmax=2.1)
#     im2 = axorg.imshow(rast_data)

    plt.title("{}".format(title), fontdict = {'fontsize': 15})  
    plt.axis('off')
    plt.colorbar(im1, fraction=0.03)
    
    