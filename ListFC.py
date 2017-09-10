# Author:  Keith Forte
# Date: 20170910
# Purpose: Assignment 2 Part III


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = r"C:\Users\Aztec_000\Desktop\Dad\Johns_Hopkins\Programming in GIS\Module 2\Module 2 Data\Newark.gdb"

# List all of the feature classes in the Newark geodatabase 
NewarkFeatureClasses = arcpy.ListFeatureClasses ()

# Iterate through all the feature classes and print the name of each feature class 
for NewarkSmellsBad in NewarkFeatureClasses:
    print(NewarkSmellsBad)

# Print "Complete"
print('Complete')

