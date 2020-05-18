from django.db import models



class EmployeeDatabase(models.Model):
    EName = models.CharField(max_length=100)
    Salary = models.IntegerField()

class CustomerDatabase(EmployeeDatabase):
    CName = models.CharField(max_length=100)
    Sales = models.IntegerField()

class StudentDatabase(CustomerDatabase):
    SName = models.CharField(max_length=100)
    Marks = models.IntegerField()
