from django.urls import path
from . import views

urlpatterns = [
    path('stores/', views.NearbyStoresView.as_view(), name='nearby-stores'),
    path('search/', views.SearchStoresView.as_view(), name='store-search'),
]
