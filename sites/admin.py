from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Site


# Register your models here.
# admin.site.register(Site, admin.OSMGeoAdmin)
@admin.register(Site)
class SiteAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')