from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from .services import get_nearby_stores

class NearbyStoresView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract latitude and longitude from the request
        lat = request.query_params.get('lat')
        lng = request.query_params.get('lng')
        
        if lat is None or lng is None:
            return Response({"error": "Latitude and Longitude are required"}, status=400)

        # Create a point from the coordinates
        user_location = Point(float(lng), float(lat), srid=4326)

        # Get nearby stores
        nearby_stores = get_nearby_stores(user_location)

        return Response(nearby_stores)
