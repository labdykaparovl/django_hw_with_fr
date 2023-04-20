from django.contrib import admin
from .models import Order
from .models import Courier

admin.site.register(Courier)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'courier')


admin.site.register(Order, OrderAdmin)

