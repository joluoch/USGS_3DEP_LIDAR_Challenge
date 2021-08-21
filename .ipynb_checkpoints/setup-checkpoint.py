from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='USGS_3DEP_LIDAR_Challenge',
  version='0.0.1',
  description='Loading USGS 3DEP data rom aws and visualizing elevation',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Jakinda Oluoch',
  author_email='jakindaodhiambo@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='lidar', 
  packages=find_packages(),
  install_requires=['pdal','geopandas','gdal'] 
)