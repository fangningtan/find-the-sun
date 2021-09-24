import json
jsonfile = r'C:\Users\fangn\PycharmProjects\sunday\data\National_Nature_Reserves_(England).geojson'

names = {}

with open(str(jsonfile)) as datafile:
    objects = json.load(datafile)
    for obj in objects['features']:
        try:
            objType = obj['type']
            if objType == 'Feature':

                properties = obj['properties']
                name = properties.get('NNR_NAME', 'no-name')
                longitude = properties.get('LONGITUDE', 0)
                latitude = properties.get('LATITUDE', 0)

                entry = {"type": "Feature",
                         "properties": {'NNR_NAME': name, 'LONGITUDE': longitude, 'LATITUDE': latitude}}

                if name not in names:
                    names[name] = entry

        except KeyError:
            pass


out_file = open("NNR_cleaned.json", "w")
json.dump(list(names.values()), out_file,  indent=2)
out_file.close()
