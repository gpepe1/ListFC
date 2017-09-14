# Author:  Michael J. Murray
# Date: 09/14/17
# Purpose:  Assignment Two


# Import ArcPy
import arcpy
 

# Set the workspace
 arcpy.env.workplace = r"C:\Users\mf8755ua.b\Dropbox\JHU\ProgrammingInGIS\Lesson-Two-PythonGithub\Newark.gdb"

# List all of the feature classes in the Newark geodatabase 
FClist = arcpy.ListFeatureClasses("*", "All")

# Iterate through all the feature classes and print the name of each feature class 
for fc in FClist:
    print fc

print "Complete"


