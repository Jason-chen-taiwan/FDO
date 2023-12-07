from django.db import models

# Create your models here.
class ownerServerInfo(models.Model):
    serverName = models.CharField(max_length=128) 
    credential = models.CharField(max_length=1000) 