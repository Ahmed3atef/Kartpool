from django.contrib.gis.db.models.functions import Distance
from .models import Store
from .serializers import NearbyStoreSerializer

def get_nearby_stores(user_location):
    # Define the radius in meters (e.g., 5000 meters = 5 kilometers)
    radius = 5000

    # Query the nearby stores within the radius
    nearby_stores = Store.objects.filter(
        location__distance_lte=(user_location, radius)
    ).annotate(
        distance=Distance('location', user_location)
    ).order_by('distance')[0:10]

    # Serialize the results
    return NearbyStoreSerializer(nearby_stores, many=True).data
