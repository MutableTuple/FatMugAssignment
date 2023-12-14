from rest_framework import serializers
from vendor.models import vendorModel, PerformanceRecord, PurchaseOrder


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model =  vendorModel
        fields = ["name","contact_details","address","on_time_delivery_rate","quality_rating_avg","average_response_time"]
        


class POSerializer(serializers.ModelSerializer):
    class Meta:
        model =  PurchaseOrder
        fields = "__all__"
        
