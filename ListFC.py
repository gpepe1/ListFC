# Author:  Charlie Shafer
# Date:  9/4/17
# Purpose:  Assignment 2


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = "C:\Users\Charlie\Google Drive\MyDocuments\AAGradSchool\Programming in GIS\Assignment2\Newark.gdb"

# List all of the feature classes in the Newark geodatabase 
fclass = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
for feature in fclass:
 print feature

# Print "Complete"
print "Complete"

