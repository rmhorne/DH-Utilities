# geoj2att.py
A quick script to parse a properties field in GeoJson into separate properties.

This was designed to address the Gephi->kml->QGIS pipeline where .kmz files produced by Gephi plugins were placing all of the attribute columns in the "description" field instead of individual properties.

This functions by calling geoj2att.py foo bar where foo is the geojson file you wish to modify and bar is the field in the geojson file that will be parsed (in my case *description*)
