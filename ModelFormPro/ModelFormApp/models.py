from django.db import models


class Customer_model(models.Model):
    Customer_name = models.CharField(max_length=100)
    Sales = models.IntegerField()
    Mobile_number = models.BigIntegerField()
    Email = models.EmailField(max_length=100)
    Location = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='content/', max_length=100, blank=True)

    def __str__(self):
        return self.Customer_name
