# grind out a dcs grid
# its so big, gotta do it in chunks

# original range: lng -150, -45 ; lat 40, 84
# split into 4:  
# 40, 62 / 62, 84
# -150, -98 / -98, -45

import arcpy
import json

print "eating polygons..."

# A list that will hold each of the Polygon objects
features = []

print "enhancing polygons..."

# 1.12 of a degree
incriment = 0.083333

def gimmiCoord(major, sub):
    if (sub == 12):
        return major + 1
    else:
        return major + (sub * incriment)

# end point is omitted in range
for lat in range(62, 84):
    print "starting lat " + str(lat)
    for lng in range(-150, -98):
        for subLat in range (0, 12):
            for subLng in range (0, 12):
                # we make a square poly branching in a positive direction from our position
                south = gimmiCoord(lat, subLat)
                north = gimmiCoord(lat, subLat + 1)
                west = gimmiCoord(lng, subLng)
                east = gimmiCoord(lng, subLng + 1)
                features.append(
                    arcpy.Polygon(
                        arcpy.Array([arcpy.Point(west, south), arcpy.Point(east, south), arcpy.Point(east, north), arcpy.Point(west, north), arcpy.Point(west, south)])))


# Persist a copy of the Polyline objects using CopyFeatures
arcpy.CopyFeatures_management(features, "c:/data/cccp/overlays/guts.gdb/grid")

print "done thanks"