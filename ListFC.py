# Author: Arin Franz
# Date: 09/09/2017
# Purpose: Listing Feature Classes


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = ("Z:\\Downloads\\Assignment2\\Newark.gdb")

# List all of the feature classes in the Newark geodatabase
listFC = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
for fc in listFC:
    print(fc)

# Print "Complete"
print("Complete")
