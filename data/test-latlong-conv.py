import unittest
from sites.helpers import parse_dms
import json

jsonfile = r'C:\Users\fangn\PycharmProjects\sunday\data\test.json'

class Tests(unittest.TestCase):
    def test_1(self):
        # Check that lat is parsed correctly
        self.assertEqual(round(parse_dms("52:47:07N"), 6), 52.785278)

    def test_2(self):
        # Check that lon is parsed correctly
        self.assertEqual(round(parse_dms("2:20:19W"), 6), -2.338611)

    def test_3(self):
        # Check that lat/long in test.json is converted correctly
        with open(str(jsonfile)) as datafile:
            objects = json.load(datafile)

            obj = objects['features'][0]
            try:
                objType = obj['type']
                if objType == 'Feature':
                    properties = obj['properties']

                    longitude = properties.get('LONGITUDE', 0)
                    latitude = properties.get('LATITUDE', 0)

                    # convert latlong
                    lat = round(parse_dms(latitude), 6)
                    lon = round(parse_dms(longitude), 6)
            except KeyError:
                pass

        self.assertEqual(lat, 52.738333)
        self.assertEqual(lon, 1.685278)


# Run each of the testing functions
if __name__ == "__main__":
    unittest.main()