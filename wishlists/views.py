from django.http import JsonResponse
from .models import WishlistItem
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import WishlistItem

def fulfill_wishlist_item(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=item_id, is_fulfilled=False)

    # Mark as fulfilled
    wishlist_item.is_fulfilled = True
    wishlist_item.save()

    # Add karma points to the user who fulfilled the request
    wishlist_item.user.add_karma_points(10)  # You can customize the points

    # Optionally, delete the fulfilled item
    wishlist_item.delete()

    return redirect(reverse_lazy('wishlist-list'))

def list_wishlists(request):
    wishlists = WishlistItem.objects.filter(is_fulfilled=False)
    return render(request, 'wishlist_list.html', {'wishlists': wishlists})