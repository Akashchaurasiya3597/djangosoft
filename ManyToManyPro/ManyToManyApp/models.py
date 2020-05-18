from django.db import models

# Create your models here.
class CompanyData(models.Model):
    Company_Name = models.CharField(max_length=100)
    Company_Email = models.EmailField(max_length=100)
    Company_Number = models.BigIntegerField()
    Company_Website = models.URLField(max_length=100)
    def __str__(self):
        return self.Company_Name

class PersonData(models.Model):
    CompanyDatahere=models.ManyToManyField(CompanyData,null=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email=models.EmailField(max_length=100)
    Mobile_Number = models.BigIntegerField()
    def __str__(self):
        return self.First_Name

