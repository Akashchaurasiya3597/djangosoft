from django.contrib import admin
from .models import Dairy_model

class AdminDairy_model(admin.ModelAdmin):
    list_display = ['Title', 'Description', 'UploadSelfie', 'UploadImage1', 'UploadImage2', 'UploadImage3']

admin.site.register(Dairy_model,AdminDairy_model)