from django.contrib import admin
from .models import vendorModel,PurchaseOrder,PerformanceRecord
# Register your models here.

admin.site.register(vendorModel)
admin.site.register(PurchaseOrder)
admin.site.register(PerformanceRecord)