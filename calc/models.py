from django.db import models

# Create your models here.
class Dest(models.Model):
    name= models.CharField(max_length=20)
    contact= models.IntegerField()
    email= models.CharField(max_length=20)
    password= models.CharField(max_length=20)