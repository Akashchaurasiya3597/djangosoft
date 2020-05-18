from django import forms
from .models import Customer_model


class Customer_Form(forms.ModelForm):
    class Meta:
        model = Customer_model
        fields = ['Customer_name', 'Sales', 'Mobile_number', 'Email', 'Location', 'picture']
