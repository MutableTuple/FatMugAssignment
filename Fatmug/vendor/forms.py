from django.forms import ModelForm, TextInput, EmailInput, Textarea, Select
from .models import vendorModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class VendorAddForm(ModelForm):
    class Meta:
        model = vendorModel
        fields = ["name","contact_details","address","vendor_code","on_time_delivery_rate","quality_rating_avg","average_response_time"]
        widgets = {
            'name': TextInput(attrs={
                'class': "vendor__form--name",
                'placeholder': 'enter name'
                }),
            'contact_details': Textarea(attrs={
                'contact_details': "vendor__form--contact",
                'placeholder': 'enter contact details'
                }), 
             'address': TextInput(attrs={
                'class': "vendor__form--address", 
                'placeholder': 'enter address'
                }),     
            'vendor_code': TextInput(attrs={
                'class': "vendor__form--vendor-code"
                }),          
            'on_time_delivery_rate': TextInput(attrs={
                'class': "vendor__form--vendor-otdr"
                }),   
            'quality_rating_avg': TextInput(attrs={
                'class': "vendor__form--vendor-qra"
                }),   
            'average_response_time': TextInput(attrs={
                'class': "vendor__form--vendor-art"
                }),   
               
        }
      
