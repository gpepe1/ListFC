# Author:  
# Date:
# Purpose:  


# Import ArcPy
import arcpy
import os


# Set the workspace
arcpy.env.workspace = "C:/Johns Hopkins/Courses/Programming in GIS/Lesson 2/Assignment2/Newark.gdb" 

# List all of the feature classes in the Newark geodatabase 
featureclasses = arcpy.ListFeatureClasses()
print(featureclasses)


# Iterate through all the feature classes and print the name of each feature class 
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []
for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        path = os.path.join(arcpy.env.workspace, ds, fc)
        print(path)

# Print "Complete"
print("Complete")


