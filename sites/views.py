from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Site



# Create your views here.

# hard code user coordinates for now
longitude = -0.18746843232914343
latitude = 51.552994052835125
user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Site
    context_object_name = 'sites'
    queryset = Site.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'sites/index.html'

home = Home.as_view()