import pdal 
import json 
import sys



def get_region_bound(Region :str , bound : str ,):
    ''' This function is going to promt a user to enter the desired region and bound'''
    PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
    pipeline_path = '../scripts/get_data.json'
    
    
    print ('===================REQUESTING REGION  =====================')
    Region = (input("Enter the Region : ")) #AI_FULLSTATE
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
    
    
    
    return Region, bound, access_path, output_filename_laz, output_filename_tif, pipeline_path

#Region = 'USGS_LPC_CO_SoPlatteRiver_Lot5_2013_LAS_2015/'
#bound = "([-11669524.7, -11666600.8], [4776607.3, 4778714.4])"
#access_path = PUBLIC_DATA_PATH + Region + 'ept.json'
#output_filename_laz = '../laz/USGS_LPC_CO_SoPlatteRiver_Lot5_2013_LAS_2015.laz'
#ouput_filename_tif = '../tif/USGS_LPC_CO_SoPlatteRiver_Lot5_2013_LAS_2015.tif'
#pipeline_path = '../scripts/get_data.json'



def get_raster_terrain(region ,bounds , access_path , output_filename_laz,ouput_filename_tif,pipeline_path ):
    
    with open(pipeline_path) as json_file:
        the_json = json.load(json_file)
        
        
    the_json['pipeline'][0]['bounds']=bounds
    the_json['pipeline'][0]['filename']=access_path
    the_json['pipeline'][5]['filename']=output_filename_laz
    the_json['pipeline'][6]['filename']=ouput_filename_tif
    
    pipeline = pdal.Pipeline(json.dumps(the_json))
    
    try:
        
        exxec = pipeline.execute()
        metadata = pipeline.metadata
        
    except RuntimeError as e :
        print(e)
        pass
      
         
if (__name__== '__main__'):
    region=sys.argv[0]
    bound=sys.argv[1]
    Region,bound,access_path,output_filename_laz,output_filename_tif,pipeline_path=get_region_bound(region,bound)
    get_raster_terrain(Region,bound,access_path,output_filename_laz,output_filename_tif,pipeline_path)
    
    

