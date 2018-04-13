# steal some geometry

import arcpy
import json

# A list of features and coordinate pairs (raw arrays)
feature_info = []

print "eating polygons..."

# open a file
with open('rawdata.json') as json_file:
    rawjson = json.load(json_file)

# crawl through the json, and extract all the separate polygons into one
# nice array of polygons
# this code is made to steal things from an arcserver identify result
# specifically, .features[].geometry.rings[]
# in the rings, take the guts and add it to our array

for feat in rawjson["features"]:
    for ring in feat["geometry"]["rings"]:
        feature_info.append(ring)

# A list that will hold each of the Polygon objects
features = []

print "enhancing polygons..."

for feature in feature_info:
    # Create a Polygon object based on the array of points
    # Append to the list of Polygon objects
    features.append(
        arcpy.Polygon(
            arcpy.Array([arcpy.Point(*coords) for coords in feature])))

# Persist a copy of the Polyline objects using CopyFeatures
arcpy.CopyFeatures_management(features, "c:/data/cccp/supportdata/fancycanada.gdb/thief")

print "done thanks"