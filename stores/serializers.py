from rest_framework import serializers
from .models import Store

class NearbyStoreSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = [
            'id', 'name', 'rating', 'opening_hour', 'closing_hour', 'store_type',
            'address', 'latitude', 'longitude', 'distance',
        ]

    def get_distance(self, obj):
        # Convert the distance to kilometers (or meters, if you prefer)
        return round(obj.distance.km, 2)  # Distance in kilometers
