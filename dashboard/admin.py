from django.contrib import admin
#from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from . models import Junkshop



@admin.register(Junkshop)
class JunkshopAdmin(LeafletGeoAdmin):
    list_display = ('shop_name', 'location')

