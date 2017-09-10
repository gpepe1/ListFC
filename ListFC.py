# Author: Colleen Livingstone  
# Date: 9/2017 
# Purpose: Assignment 2  


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = r"C:\Users\Colleen\Documents\GRAD GIS\Programming\Data\Assignment2\Newark.gdb"
 

# List all of the feature classes in the Newark geodatabase
fcList = arcpy.ListFeatureClasses()


# Iterate through all the feature classes and print the name of each feature class
for fc in fcList:
    print (fc)


# Print "Complete"
print ("Complete")


