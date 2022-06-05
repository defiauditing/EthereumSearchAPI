from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from enum import IntEnum

class Permium(models.IntegerChoices):
    FREE = 0
    PREMIUM = 1
class Profile(models.Model):
    PREMIUM_CHOICES = (("FREE",0),("PREMIUM",1))
    user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    premium = models.IntegerField(choices=Permium.choices,default=0)
    due_date = models.DateField(null=True)

class AnaysisStatus(models.IntegerChoices): #TODO
    PENDING = 1
    COMPLETED = 2
    FAILED = 0

    
class Analysis(models.Model):
    STATUS_CHOICES = ((1,"PENDING"),(2,"COMPLETED"),(0,"FAILED"))
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.IntegerField(choices=AnaysisStatus.choices,null= True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    file = models.FileField(null=True)
    data  = models.JSONField(null=True)
    stdout = models.TextField(null=True)

