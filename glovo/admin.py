from django.contrib import admin
from .models import Order
from .models import Courier

admin.site.register(Courier)


admin.site.register(Order)

