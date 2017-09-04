# Author: Jesse Peterson
# Date: 09/04/2017
# Purpose: The purpose of this script is to test 


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = r"C:\Users\jrpete\JHU_COURSES\Programming_In_GIS\Lesson2_Python_ArcGIS_Basics\Assignment2\Assignment2\Newark.gdb"

# List all of the feature classes in the Newark geodatabase 
featureclasses = arcpy.ListFeatureClasses()
print(featureclasses)

# Iterate through all the feature classes and print the name of each feature class 
for fc in featureclasses:
    print(fc)

# Print "Complete"
print("complete")

