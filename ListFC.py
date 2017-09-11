# Author:  
# Date:
# Purpose:  


# Import ArcPy
import arcpy
 

# Set the workspace
 
 arcpy.env.workspace = "C:/Users/bmocci/Desktop/JHU/Programming in GIS/Module 2/Assignment2/LasVegas.gdb"
 
# List all of the feature classes in the Newark geodatabase 

arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 

for features in FeatureClasses:
    print(features)
	
# Print "Complete"

print('Complete')
