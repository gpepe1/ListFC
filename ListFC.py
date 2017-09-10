# Author:  Chris Rehak
# Date: August 9th, 2017
# Purpose:  Lesson 2, Part 3 - GitHub


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = r"C:\Users\CRehak\Desktop\Hopkins\Programming in GIS\Module 2\Assignment2\Assignment2\Newark.gdb"

# List all of the feature classes in the Newark geodatabase
featureclass = arcpy.ListFeatureClasses()


# Iterate through all the feature classes and print the name of each feature class
for feature in featureclass:
    print(feature)
    
# Print "Complete"
print ("Complete")


