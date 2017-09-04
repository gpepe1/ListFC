# Author:  Jason Lowe
# Date:  September 4, 2017
# Purpose:  Complete Part III of the Homework Assignment for Module 2 (Johns Hopkins University - Course 606)


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = r"C:\Users\Jason\Desktop\School\606 Information\Module 2\Data for Assignment 2\Assignment2\Newark.gdb"
 

# List all of the feature classes in the Newark geodatabase
# fcList is a Python list returned from the ListWorkspaces function 
fcList = arcpy.ListFeatureClasses()


# Iterate through all the feature classes and print the name of each feature class 
for fc in fcList:
	print fc

# Print "Complete"
print "Complete"

