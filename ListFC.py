# Author:   James Jones
# Date:     5 September 2016
# Purpose:  To iterate through a workspace and pring the names of feature classes.


# Import ArcPy
import arcpy
from arcpy import env


# Set the workspace
env.workspace = r'C:\Student\AS.430.606\Assignment2\Assignment2\Newark.gdb'

# List all of the feature classes in the Newark geodatabase
fc = arcpy.ListFeatureClasses("*")

# Iterate through all the feature classes and print the name of each feature class
for f in fc:
    print(f)

# Print "Complete"
print("Complete")