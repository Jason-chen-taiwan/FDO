from django.db import models

# Create your models here.
class ownerServerInfo(models.Model):
    serverName = models.CharField(max_length=128) 
    credential = models.CharField(max_length=1000)
    rpbelong = models.CharField(max_length=128)

class ClientMachine(models.Model):
    serial_no = models.CharField(max_length=50)  
    guid = models.CharField(max_length=50,unique=True)  
    di_timestamp = models.DateTimeField()
    attestation_type = models.CharField(max_length=128) 