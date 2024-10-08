from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Inventory(models.Model):
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name
class Store(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    rating = models.IntegerField(null = True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    store_type = models.CharField(null=True, max_length=50)
    opening_hour = models.TimeField(null=True)
    closing_hour = models.TimeField(null=True)
    city = models.CharField(max_length=50)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    location = models.PointField(null=True, srid=4326)
    address = models.CharField(max_length=100)
    phone = models.CharField(null=True, max_length=100)
    inventory = models.ManyToManyField(Inventory)
    
    def __str__(self):
        return self.name