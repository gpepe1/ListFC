# Author: Katie Tartaglia 
# Date: 9/5/2017
# Purpose:606 Assignment 2


# Import ArcPy
import arcpy

# Set the workspace
arcpy.env.workspace = r"C:\606\Assignment2\Newark.gdb"

# List all of the feature classes in the Newark geodatabase 
featureclasses = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
for FCs in featureclasses:
    print FCs

# Print "Complete"
print "Complete"

