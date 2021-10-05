from django.test import TestCase, Client
from django.contrib.gis.geos import Point
from .models import Site

# Create your tests here.
class SiteTestCase(TestCase):
    def setUp(self):
        # Create sites
        # location is (lon,lat)
        s1 = Site.objects.create(name="Site1", location=Point((-0.188133,51.553027)))
        s2 = Site.objects.create(name="Site2", location=Point((-0.274574, 51.441352)))

        # add site outside of 50 km radius
        s3 = Site.objects.create(name="Site3", location=Point((103.860608,1.285434)))


    def test_index(self):
        # Set up client to make requests
        c = Client()

        # Send get request to index page and store response
        response = c.get("")

        # Make sure status code is 200
        self.assertEqual(response.status_code, 200)

        # Make sure queryset contains the correct number of sites
        # Since s3 is outside of the 100km radius, it should not be present in the queryset
        # Note: this works only with the currently hardcoded user_location var in views.py
        # consider writing another more dyanamic test in the future?
        # print(response.context['sites'])
        self.assertEqual(response.context['sites'].count(), 2)
