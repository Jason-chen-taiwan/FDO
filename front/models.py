from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identity = models.CharField(max_length=255)  # 或者使用更合适的字段类型
