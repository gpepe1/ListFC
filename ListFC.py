# Author:  Paul Lukas
# Date:  9-9-17
# Purpose:  To list the geodatabases in a workspace


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = "C:/Users\Paul\Documents\Education\Johns Hopkins\Classes\Programming in GIS AS 430 606\Lessons\Assignment 2\Assignment2(1)\Assignment2\Newark.gdb"
 
# List all of the feature classes in the Newark geodatabase 
GDB = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
For FC in GDB:
    print(FC)

# Print "Complete"
print("Complete")


