# Author:  Joshua Boerma
# Date: 6 Sep 2017
# Purpose:  For assignment 2 in Programming in GIS


# Import ArcPy
import arcpy
 

# Set the workspace
 arcpy.env.workspace = r'E:\GIS\School\3Programming\Assignment2(1)\Assignment2\Newark.gdb'

# List all of the feature classes in the Newark geodatabase 
arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
features = arcpy.ListFeatureClasses()
for feat in features:
    print feat

# Print "Complete"
print "Complete"

