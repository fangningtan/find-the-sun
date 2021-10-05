from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.core.serializers import serialize

from .models import Site
from capstone.settings import MAPBOX_TOKEN



# Create your views here.

# hard code user coordinates for now
longitude = -0.18746843232914343
latitude = 51.552994052835125
user_location = Point(longitude, latitude, srid=4326)
radius = 50


class Home(generic.ListView):
    model = Site
    context_object_name = 'sites'
    # filter for 6 nearest points to specified location
    # queryset = Site.objects.annotate(distance=Distance('location',
    # user_location)
    # ).order_by('distance')[0:6]

    # filter for objects within given radius
    within_radius = Site.objects.filter(location__distance_lte=(user_location, D(km=radius)))
    # then order by distance
    queryset = within_radius.annotate(distance=Distance('location', user_location)).order_by('distance')
    template_name = 'sites/index.html'

home = Home.as_view()


# map view
def default_map(request):
    # TODO: add url restrictions when deployed to production
    mapbox_access_token = MAPBOX_TOKEN

    # filter for nearest sites within radius
    results = Site.objects.filter(location__distance_lte=(user_location, D(km=radius)))
    # Note: it seems like the geometry_field argument is the name of the field containing the point
    result_json = serialize('geojson', results,
              geometry_field='location',
              fields=('name',))

    return render(request, 'sites/default.html',
                  {'mapbox_access_token': mapbox_access_token,
                   'results_json': result_json,
                   'results': results}
                  )