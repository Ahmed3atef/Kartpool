from django.urls import path
from .views import fulfill_wishlist_item, list_wishlists

urlpatterns = [
    path('wishlists/', list_wishlists, name='wishlist-list'),
    path('wishlists/fulfill/<int:item_id>/', fulfill_wishlist_item, name='fulfill-wishlist'),
]
