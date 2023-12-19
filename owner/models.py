from django.db import models

# Create your models here.
class machine(models.Model):
    guid = models.CharField(max_length=50,unique=True)  
    to0_timestamp = models.DateTimeField(null=True)
    to2_timestamp = models.DateTimeField(null=True)
    owner = models.CharField(max_length=128)