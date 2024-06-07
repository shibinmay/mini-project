from django.db import models

# Create your models here.

class home(models.Model):
    fullname=models.CharField(max_length=99)
    email=models.CharField(max_length=99)
    username=models.CharField(max_length=99)
    password=models.IntegerField()
    Aadhar=models.IntegerField()
    Place=models.CharField(max_length=99)
    Age=models.IntegerField(null=True,blank=True)
    initialamount=models.IntegerField()

    def __str__(self):
        return self.fullname
