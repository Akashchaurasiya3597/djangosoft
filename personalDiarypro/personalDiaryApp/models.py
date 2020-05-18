from django.db import models



class Dairy_model(models.Model):
    id = models.AutoField
    Title = models.CharField(max_length=100,null=True)
    Description = models.CharField(max_length=200,null=True)
    UploadSelfie = models.ImageField(upload_to='content/', blank=True, max_length=100)
    UploadImage1 = models.ImageField(upload_to='content/', blank=True, max_length=100)
    UploadImage2 = models.ImageField(upload_to='content/', blank=True, max_length=100)
    UploadImage3 = models.ImageField(upload_to='content/', blank=True, max_length=100)
    Date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Title


