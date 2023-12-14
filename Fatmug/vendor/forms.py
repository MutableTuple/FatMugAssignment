from django.forms import ModelForm, TextInput, EmailInput, Textarea, Select
from .models import vendorModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class VendorAddForm(ModelForm):
    class Meta:
        model = vendorModel
        fields = "__all__"
      
