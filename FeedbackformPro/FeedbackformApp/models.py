from django.db import models

class FeedbackDatabase(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Mobile = models.BigIntegerField()
    ratting = models.IntegerField()
    Data = models.DateTimeField()
    Feedback = models.CharField(max_length=100)


