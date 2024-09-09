from django.db import models
from django.conf import settings
from stores.models import Store, Inventory

class WishlistItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item = models.ManyToManyField(Inventory)
    karma = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        items = [item.item_name for item in self.item.all()]
        return f"{self.user} want {items} from {self.store.name}"
