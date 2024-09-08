from django.views.generic import TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from stores.models import Store


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url='login'
    


class StoreDetailView(DetailView):
    model = Store
    template_name = 'store_detail.html'
    context_object_name = 'store'
    
    
