import re
import json
from pathlib import Path


def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes) / 60 + float(seconds) / (60 * 60);
    if direction == 'W' or direction == 'S':
        dd *= -1
    return dd;


def dd2dms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, sd]


def parse_dms(dms):
    # split up the DMS string into four parts
    parts = re.findall(r'[A-Za-z]+|\d+', dms)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])

    return (lat)


jsonfile = r'C:\Users\fangn\PycharmProjects\sunday\data\test.json'

with open(str(jsonfile)) as datafile:
    objects = json.load(datafile)
    for obj in objects['features']:
        try:
            objType = obj['type']
            if objType == 'Feature':
                properties = obj['properties']
                name = properties.get('NNR_NAME', 'no-name')

                # TODO convert latlong to correct format
                longitude = properties.get('LONGITUDE', 0)
                latitude = properties.get('LATITUDE', 0)

                # convert latlong
                lat = round(parse_dms(latitude),6)
                lon = round(parse_dms(longitude),6)

                print(f'{lat}, {lon}')
        except KeyError:
            pass
DATA_FILENAME = 'National_Nature_Reserves_(England).geojson'
print(Path(__file__).parents[1] / DATA_FILENAME)