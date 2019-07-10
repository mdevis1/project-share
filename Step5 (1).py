# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:42:59 2019

@author: devis

"""

import gmplot 
import csv
latitude_list=[]
longitude_list=[]
with open('traffic_violations (2).csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',')
    for data in reader:
        
      if data['Belt'] == 'Yes':
        latitude_list.append(float(data['Latitude']))
        longitude_list.append(float(data['Longitude']))
        
  
gmap3 = gmplot.GoogleMapPlotter(39.0458, 
                               -76.6413, 10) 


gmap3.heatmap( latitude_list, longitude_list ) 
gmap3.draw( "C:\\Users\\devis\\Desktop\\Belt.html" ) 