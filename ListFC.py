# Author:  Sean D. Grube
# Date: 07SEP2017
# Purpose:  List feature classes within a geodatabase


# Import ArcPy
import arcpy

# Set the workspace
arcpy.env.workspace = r'E:\Documents\!JHU\606 Programming in GIS\Module 2\Assignment2\Assignment2\Newark.gdb'

# List all of the feature classes in the Newark geodatabase 
fcList = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
for fc in fcList:
    print(fc)

# Print "Complete"
print('Complete')

