
from rest_framework import serializers
from .models import Wishlist, WishlistItem

class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = ['store_item', 'quantity']

class WishlistSerializer(serializers.ModelSerializer):
    items = WishlistItemSerializer(many=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        wishlist = Wishlist.objects.create(**validated_data)
        for item_data in items_data:
            WishlistItem.objects.create(wishlist=wishlist, **item_data)
        return wishlist
