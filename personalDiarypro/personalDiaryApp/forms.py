from django import forms
from .models import Dairy_model

class Diary_form(forms.ModelForm):
    class Meta:
        model = Dairy_model
        fields = ['Title', 'Description', 'UploadSelfie', 'UploadImage1', 'UploadImage2', 'UploadImage3']


