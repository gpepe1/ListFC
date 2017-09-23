# Author: Stessy Cocerez
# Date: 09/23/2017
# Purpose:  Assignment 2


# Import ArcPy
import ArcPy
 

# Set the workspace
arcpy.env.workspace = "C:\\AS.430.606.82.FA17 Programming in Gis\\Assignment2\Newark.gdb"

# List all of the feature classes in the Newark geodatabase 
fclist = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
for fc in fclist:
    print(fc)

# Print "Complete"
print "Complete"
