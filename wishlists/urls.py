from django.urls import path
from .views import fulfill_wishlist_item, list_wishlists,add_to_wishlist,delete_wishlist

urlpatterns = [
    path('wishlists/', list_wishlists, name='wishlist-list'),
    path('wishlists/fulfill/<int:item_id>/', fulfill_wishlist_item, name='fulfill-wishlist'),
    path('add/<int:item_id>/<int:store_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('delete/<int:wishlist_id>/', delete_wishlist, name='delete-wishlist'),
]
