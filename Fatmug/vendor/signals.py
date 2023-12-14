import pytz
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import vendorModel,PurchaseOrder, PerformanceRecord
from datetime import datetime, date
from django.utils import timezone

vmodel = vendorModel.objects.all()
# def increment_rate(sender, instance, created, **kwargs):
#     # if not created and instance.status == "completed":
#         # Disconnect the signal temporarily to avoid recursion
#         post_save.disconnect(increment_rate, sender=vendorModel)

#         # Update the delivery_date and save the instance
#         instance.total_po_completed+=1
#         instance.save()

def is_completed(sender, instance, created, **kwargs):
    if not created and instance.status == "completed":
        # Disconnect the signal temporarily to avoid recursion
        post_save.disconnect(is_completed, sender=PurchaseOrder)

        # Update the delivery_date and save the instance
        instance.delivery_date = timezone.now()
        instance.vendor.total_po_completed+=1
        if instance.delivery_date<=instance.estimated_delivery_date:
            instance.delivered_before_delivery_date=1
            
        else: instance.delivered_before_delivery_date=0
        instance.save()
    


        # Reconnect the signal
    

post_save.connect(is_completed, sender=PurchaseOrder)