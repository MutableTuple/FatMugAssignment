import secrets
import string
from django.db import models

# vendor code genrator

def generate_unique_code():
      code = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(5))
      return code
    

# Create your models here.
class vendorModel(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    vendor_code = models.CharField(max_length=15, blank=True, null=True, default=generate_unique_code())
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg= models.FloatField()
    average_response_time = models.FloatField()
    # extra fields
    total_po_completed = models.IntegerField(default=0)
    total_po_cancelled = models.IntegerField(default=0)
    total_po_pending = models.IntegerField(default=0)
    fulfillment_rate = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        total_po_sum = self.total_po_completed + self.total_po_cancelled + self.total_po_pending

        # Avoid division by zero
        if total_po_sum > 0:
            self.fulfillment_rate = (self.total_po_completed / total_po_sum) * 100
        else:
            self.fulfillment_rate = 0.0

        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}({self.vendor_code})"

    
class PurchaseOrder(models.Model):
    CLASSIFICATION_CHOICES =dict({
        "FR": "Freshman",
        "SO": "Sophomore",
        "JR": "Junior",
        "SR": "Senior",
        "GR": "Graduate",
    })

    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(vendorModel, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    # custom fiels
    estimated_delivery_date = models.DateTimeField(null=True, blank=True)
    delivered_before_delivery_date = models.IntegerField(default=0, null=True, blank=True)
    items = models.JSONField(default=CLASSIFICATION_CHOICES)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20,null=True, blank=True,choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ])
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO {self.po_number} - {self.vendor.name}"


class PerformanceRecord(models.Model):
    vendor = models.ForeignKey(vendorModel, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    
    def __str__(self):
        return f"{self.vendor.name}({self.on_time_delivery_rate})"
