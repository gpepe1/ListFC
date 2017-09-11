# Author:  Daniel Cassiday
# Date: 9/10/17
# Purpose:  Programming in GIS


import arcpy

arcpy.env.workspace = r"C:\Users\DC\Documents\GIS\4. Fall 2017\Programming in GIS\Week 2\Assignment2(1)\Assignment2"

fcList = arcpy.ListFeatureClasses("","","Newark.gdb")

for fc in fcList:
    print (fc)

print ("Complete")