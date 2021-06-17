from django import forms
from django.forms import ModelForm, fields
from .models import foodDonation, moneyDonation

class FoodDonationForm(ModelForm):
    class Meta:
        model = foodDonation
        fields = ['country', 'state', 'city', 'location', 'contactno', 'quantity', 'food_type']

class MoneyDonateForm(ModelForm):
    class Meta:
        model = moneyDonation
        fields = ['amount', 'contactno']