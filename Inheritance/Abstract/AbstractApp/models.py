from django.db import models
class Commandatabase(models.Model):
    Name = models.CharField(max_length=100)
    Mobile = models.BigIntegerField()
    Email = models.EmailField(max_length=100)
    class Meta:
        abstract = True

class EmployeeDatabase(Commandatabase):
    Salary = models.IntegerField()
    def __str__(self):
        return self.Name
class CustomerDatabase(Commandatabase):
    Sales = models.IntegerField()
    def __str__(self):
        return self.Name
class StudentDatabase(Commandatabase):
    Marks = models.IntegerField()
    def __str__(self):
        return self.Name