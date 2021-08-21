import pdal 
import json 
import sys
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd

def get_region_bound(Region :str , bound : str ,):
    ''' 
    This function is going to promt a user to enter the desired region and bound
    
    The out put expectd is : the Region, the bound, the aws public path, the laz output file path, the tif file path and the csv file path
    
    
    
    '''
    
    PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
    pipeline_path = '../scripts/get_data.json'
    
    
    print ('===================REQUESTING REGION  =====================')
    Region = (input("Enter the Region : ")) #IA_FullState
    print (Region)
    
    
    print ('===================REQUESTING  BOUNDS =====================')
    bound = (input("Enter the Bounds [MINX, MINY, MAXX, MAXY] : ")) #bound = "([-11669524.7, -11666600.8], [4776607.3, 4778714.4])"
    print(bound)
    
    print ('===================REQUEST PATH =====================')
    access_path = PUBLIC_DATA_PATH + Region + '/ept.json'
    print(access_path)
    
    print ('===================OUPUT LAZ PATH =====================')
    output_filename_laz = "../laz/"+Region+".laz"
    print(output_filename_laz)
    
    print ('===================OUPUT TIF PATH =====================')
    output_filename_tif = "../tif/"+Region+".tif"
    print(output_filename_tif)
    
    print ('===================OUPUT CSV PATH =====================')
    output_filename_csv = "../csv/"+Region+".csv"
    print(output_filename_csv)
    
    
    return Region, bound, access_path, output_filename_laz, output_filename_tif,output_filename_csv,pipeline_path

#Region = 'USGS_LPC_CO_SoPlatteRiver_Lot5_2013_LAS_2015/'
#bound = "([-11669524.7, -11666600.8], [4776607.3, 4778714.4])"
#([-93.756155, 41.918015],[ -93.747334, 41.921429])
#access_path = PUBLIC_DATA_PATH + Region + 'ept.json'
#output_filename_laz = '../laz/USGS_LPC_CO_SoPlatteRiver_Lot5_2013_LAS_2015.laz'
#ouput_filename_tif = '../tif/USGS_LPC_CO_SoPlatteRiver_Lot5_2013_LAS_2015.tif'
#pipeline_path = '../scripts/get_data.json'



def get_raster_terrain(region ,bounds , access_path , output_filename_laz,ouput_filename_tif,output_filename_csv,pipeline_path):#output_filename_geojson
    
    """
    Queries the pdal json pipelin and fill the bound and filename paths accordingly then generated the data 
    """
    
    with open(pipeline_path) as json_file:
        the_json = json.load(json_file)
        
        print ('===================filling pdal json file  =====================')
    the_json['pipeline'][0]['bounds']=bounds
    the_json['pipeline'][0]['filename']=access_path
    the_json['pipeline'][6]['filename']=output_filename_laz
    the_json['pipeline'][7]['filename']=ouput_filename_tif
    the_json['pipeline'][8]['filename']=output_filename_csv
    print ('===================dumping the json file, saving .tif,.laz.csv =====================')
    pipeline = pdal.Pipeline(json.dumps(the_json))
    
    try:
        
        exxec = pipeline.execute()
        metadata = pipeline.metadata
        
    except RuntimeError as e :
        print(e)
        pass

def geometry (csvpath,region): 
    """
    takes the cvs output file and generates a geodataframe with the elevation and coordinates of every point 
    """
    print ('===================READING CSV  =====================')
    pan = pd.read_csv(csvpath)
    
    geo = pan[["X","Y","Z"]]
    
    #convert xyz to geodataframe
    geometry = [Point(xy) for xy in zip(pd.to_numeric(geo['X']), pd.to_numeric(geo['Y']))]
    gdf = gpd.GeoDataFrame(geo, crs='epsg:4326',geometry=geometry)
    gdf = gdf[["Z", "geometry"]]
    gdf = gdf.rename(columns={"Z": "elevation_m", "geometry": "geometry"})
    gdf.to_csv("../csv/"+region+".csv")
    
    return gdf  
         
if (__name__== '__main__'):
    region=sys.argv[0]
    bound=sys.argv[1]
    Region,bound,access_path,output_filename_laz,output_filename_tif,output_filename_csv,pipeline_path=get_region_bound(region,bound)
    get_raster_terrain(Region,bound,access_path,output_filename_laz,output_filename_tif,output_filename_csv,pipeline_path)
    geometry(output_filename_csv,Region)
    
    

