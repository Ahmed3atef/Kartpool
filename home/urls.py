from django.urls import path
from .views import HomePageView,StoreDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('store/<int:pk>', StoreDetailView.as_view(), name="store-into"),
]
