# Author:  Jonathan Hughes
# Date:  20170907
# Purpose:  Assignment 2 Python for GIS and ArcPy Basics


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = "C:\\Users\\Jon\\OneDrive - Johns Hopkins University\\AS_430_606_GIS_Programming\\Assignment_2\Newark.gdb"

# List all of the feature classes in the Newark geodatabase 
FCList = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
for FC in FCList:
    desc = arcpy.Describe(FC) 
    print(desc.name)

# Print "Complete"
print("Complete")

