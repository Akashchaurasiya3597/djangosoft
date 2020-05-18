from django.db import models



class EmployeeDatabase(models.Model):
    Eid=models.AutoField(primary_key=True)
    EName = models.CharField(max_length=100)
    Salary = models.IntegerField()

class CustomerDatabase(models.Model):
    Cid=models.AutoField(primary_key=True)
    CName = models.CharField(max_length=100)
    Sales = models.IntegerField()

class StudentDatabase(EmployeeDatabase,CustomerDatabase):
    Sid=models.AutoField(primary_key=True)
    SName = models.CharField(max_length=100)
    Marks = models.IntegerField()

