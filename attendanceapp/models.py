from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class attendee(models.Model):
   Name= models.CharField(max_length=50)
   batch= models.CharField(max_length=10)
   enrollmentno=models.CharField(max_length=20)
   branch= models.CharField(max_length=5)




class workshopdetails(models.Model):
    Title = models.CharField(max_length=40)
    Details = models.TextField()
    LastRegisterDate=models.DateTimeField(blank=True)
    NoofPeopleRegistered=models.IntegerField(default=0)
    attendee1=models.ForeignKey(attendee,on_delete=models.CASCADE,blank=True,null=True)
    currentuserattending=models.TextField(default="No")