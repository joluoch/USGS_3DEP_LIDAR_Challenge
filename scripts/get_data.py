import pdal 
import json 

PUBLIC_DATA_PATH = 'https://s3-us-west-2.amazonaws.com/usgs-lidar-public/'

Region = 'IA_FullState/'

bound = "([-10425171.940, -10423171.940], [5164494.710, 5166494.710])"

access_path = PUBLIC_DATA_PATH + Region + 'ept.json'

output_filename_laz = '../laz/iowa.laz'
ouput_filename_tif = '../tif/iowa.tif'
pipeline_path = '../scripts/get_data.json'


def get_raster_terrain(bounds=bound , region=Region, public_access_path = PUBLIC_DATA_PATH,
                      output_filename_laz=output_filename_laz,ouput_filename_tif =ouput_filename_tif,pipeline_path =pipeline_path ):
    
    with open(pipeline_path) as json_file:
        the_json = json.load(json_file)
        
        
    the_json['pipeline'][0]['bounds']=bounds
    the_json['pipeline'][0]['filename']=public_access_path
    the_json['pipeline'][6]['filename']=output_filename_laz
    the_json['pipeline'][7]['filename']=ouput_filename_tif
    
    pipeline = pdal.Pipeline(json.dumps(the_json))
    
    try:
        
        exxec = pipeline.execute()
        metadata = pipeline.metadata
        
    except RuntimeError as e :
        print(e)
        pass
        
         
if (__name__== '__main__'):
    get_raster_terrain()
    
    

