from django import forms
from .models import FeedbackDatabase
class FeedbackForm(forms.Form):
    First_name = forms.CharField(
        label='Enter the First name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter the your  first name'
            }
        )
    )
    Last_name = forms.CharField(
        label='Enter the last name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Enter the your last name'
            }

        )
    )
    Email = forms.EmailField(
        label='Enetr the your Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter the your Email'
            }
        )
    )
    Mobile = forms.IntegerField(
        label='Enter the mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter the Mobile number'
            }
        )
    )
    ratting = forms.IntegerField(
        label='Enter the ratting',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your ratting'
            }
        )

    )
    Feedback = forms.CharField(
        label='Enter your precious feedback:',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your ratting'
            }
        )
    )

