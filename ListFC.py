# Author:  Donald Shaw
# Date: 09/02/2017
# Purpose:  To Learn GitHub


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = "C:/EsriTraining/Assignment2/newark.gdb"

# List all of the feature classes in the Newark geodatabase 
fc = arcpy.ListFeatureClasses()


# Iterate through all the feature classes and print the name of each feature class 
for featureclasses in fc:
    print(fc)
	
# Print "Complete"
print("Complete")



