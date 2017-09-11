# Author:  Andrew Ziminski
# Date: 9/10/2017
# Purpose:  assignment 2


# Import ArcPy
import arcpy
 

# Set the workspace
 
arcpy.env.workspace = r"C:\Users\andre\Desktop\Programming\Assignment 2\Assignment2\Newark.gdb"

# List all of the feature classes in the Newark geodatabase 
featureclasses = arcpy.ListFeatureClasses()

	

# Iterate through all the feature classes and print the name of each feature class 

for features in featureclasses:
	print features

# Print "Complete"

print ("Complete")

