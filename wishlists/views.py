from django.http import JsonResponse
from .models import WishlistItem
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import WishlistItem
from django.contrib.auth.decorators import login_required
from stores.models import Store, Inventory

@login_required
def fulfill_wishlist_item(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=item_id)

    # Add karma points to the user who done the request
    wishlist_item.user.add_karma_points(wishlist_item.karma) 

    # Optionally, delete the fulfilled item
    wishlist_item.delete()

    return redirect(reverse_lazy('wishlist-list'))

@login_required
def add_to_wishlist(request, item_id, store_id):
    if request.method == "POST":
        
        store_item = get_object_or_404(Inventory, id=item_id)
        store = get_object_or_404(Store, id=store_id)

        # Create or get the WishlistItem for the current user and store (without adding items yet)
        wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, store=store)

        # Now add the store item to the WishlistItem's ManyToMany field (item)
        wishlist_item.item.add(store_item)  # Add store item to the ManyToManyField

        # Optionally, update karma points if necessary
        wishlist_item.karma = request.POST.get('karma')
        wishlist_item.save()

        # Redirect to the wishlist view or another success page
        return redirect('wishlist-list')

@login_required
def delete_wishlist(request, wishlist_id):
    wishlist_item = get_object_or_404(WishlistItem, id=wishlist_id)

    # Check if the logged-in user is the owner of the wishlist
    if wishlist_item.user == request.user:
        wishlist_item.delete()

    # Redirect to the wishlist page after deletion
    return redirect('wishlist_view')

@login_required
def list_wishlists(request):
    wishlists = WishlistItem.objects.all()
    return render(request, 'wishlist_list.html', {'wishlists': wishlists})