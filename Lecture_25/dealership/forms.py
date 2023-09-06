from django import forms
from .models import Dealer, Brand, Car
from django.forms import DateTimeInput


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'car_model', 'speed', 'picture']




class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = ['name', 'surname', 'birth_day', 'dealer_of']
