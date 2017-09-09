# Author:  Alex Metzler
# Date: 9 Septemeber 2017
# Purpose:  Module 2 Assignment


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = "C:/Users/ametz_000/Google Drive/GIS/MGIS_JHU/Programming/Module2/Assignment2/Assignment2/Newark.gdb"


# List all of the feature classes in the Newark geodatabase 
featureclasses = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
for i in featureclasses:
    print (i)

# Print "Complete"

print ("complete")
