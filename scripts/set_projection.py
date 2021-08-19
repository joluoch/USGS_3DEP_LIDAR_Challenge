import os 
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import earthpy as et




def set_projection(shpfile):
    file = gpd.read_file(shpfile)
    file = file.set_crs('epsg:26915')
    #print(file.crs)
    
    return file