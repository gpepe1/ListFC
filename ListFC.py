# Author:  Peter Klingman
# Date: 09/06/2017
# Purpose:  Practice with GitHub


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = "c:\\Assignments\\Programming_in_GIS_Fall_17\\Assignment2\\Newark.gdb"

# List all of the feature classes in the Newark geodatabase 
feature_classes = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
for feature_class in feature_classes:
    print feature_class

# Print "Complete"
print "Complete"


