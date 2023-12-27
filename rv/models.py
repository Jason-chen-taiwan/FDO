from django.db import models

# Create your models here.
class to0_information(models.Model):
    guid = models.CharField(max_length=50)  
    to0_time = models.DateTimeField(null=True)
    owner_name = models.CharField(max_length=50)