#Parser to take geosjon attributes and split them out, This is for the kml->geojson pipline to prserve attribute data1

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#finish up the imports we need
import json

#grab the attribute value holder from the command prompt
attributeHolder = sys.argv[2]

#grab the geojson file from the command prompt
geojsonFile = sys.argv[1]


with open(geojsonFile) as f:
    data = json.load(f)

dict = {}
finalDict = {}

for feature in data['features']:
    toSplit = feature['properties'][attributeHolder].split('\n')

    for v in toSplit:
        #had a problem with empty values
        if v != '':
            aux = v.split(":")
            dict[aux[0]] = aux[1]
    finalDict = feature['properties']
    del finalDict[attributeHolder]
    finalDict.update(dict)

#output file name
outputFileName = "%s[geoJsonAttributeFix].geojson" % (sys.argv[1].split(".")[0])

with open(outputFileName, 'w') as f:
    json.dump(data, f)
