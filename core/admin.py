from django.contrib import admin
from .models import Item,OrderItem,Order

admin.site.site_header = "Lynn's Unique Collection"
admin.site.site_title = "Lynn's Unique Collection"

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)