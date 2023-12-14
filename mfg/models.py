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
    clientbelong = models.CharField(max_length=128)
    
class OwnershipVoucher(models.Model):
    serverName = models.ForeignKey(ownerServerInfo, on_delete=models.CASCADE, related_name='vouchers')
    serial_no = models.ForeignKey(ClientMachine, on_delete=models.CASCADE, related_name='vouchers')
    create_time = models.DateTimeField(auto_now_add=True)  # 修改为 DateTimeField 并设置 auto_now_add
    ownership_voucher = models.CharField(max_length=512)
    clientbelong = models.CharField(max_length=128)