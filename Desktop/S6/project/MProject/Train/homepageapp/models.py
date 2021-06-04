from django.db import models

# Create your models here.


# Create your models here.
class reg_tbl(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    eml = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    paswd=models.CharField(max_length=100)

class adminlogin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
