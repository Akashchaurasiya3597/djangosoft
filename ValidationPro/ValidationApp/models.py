from django.db import models

class RegistrationModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    mobile_number = models.BigIntegerField()


