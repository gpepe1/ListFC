# Author:  Greg McFadden
# Date: 9/5/2017
# Purpose:  GitHub exercise


# Import ArcPy
import arcpy
 
# Set the workspace
arcpy.env.workspace = "C:\\Assignment2\\Newark.gdb"

# List all of the feature classes in the Newark geodatabase
listfc = arcpy.ListFeatureClasses()
print (listfc)

# Iterate through all the feature classes and print the name of each feature class 
for fc in arcpy.ListFeatureClasses():
    print (fc)

# Print "Complete"
print ("Complete")


