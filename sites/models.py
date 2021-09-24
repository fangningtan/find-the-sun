from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Site(models.Model):
    # TODO should the name be unique?
    name = models.CharField(max_length=100, unique=True)
    location = models.PointField()

