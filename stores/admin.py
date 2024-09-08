from django.contrib.gis.admin import GISModelAdmin
from django.contrib import admin
from .models import Store, Inventory

@admin.register(Store)
class SotreAdmin(GISModelAdmin):
    list_display = ('id','created_at', 'name', 'rating', 'store_type', 'city', 'latitude', 'longitude', 'location', 'address', 'phone')
    
admin.site.register(Inventory)