from django.db import models

# Create your models here.
class EmployeeDatabase(models.Model):
    Name = models.CharField(max_length=100)
    Mobile = models.BigIntegerField()
    Email = models.EmailField(max_length=100)
    Salary = models.IntegerField()

class ProxyDatabase(EmployeeDatabase):
    class Meta:
        proxy = True

