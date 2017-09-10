# Author:  Alex Hutcheson
# Date: 9/9/17
# Purpose:  Assignment 2 Programming in GIS


# Import ArcPy
import arcpy


# Set the workspace
arcpy.env.workspace = r"C:\Users\HP Envy 17 Touch\Documents\Programming\Assignment2\Assignment2\Newark.gdb"


# List all of the feature classes in the Newark geodatabase
fcList = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class

for fc in fcList:
    desc = arcpy.Describe(fc)
    print desc.name


# Print "Complete"

print "Complete"
