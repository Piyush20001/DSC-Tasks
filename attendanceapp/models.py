from django.db import models
from django.utils import timezone


class attendee(models.Model):
   Name= models.CharField(max_length=50)
   batch= models.CharField(max_length=10)
   enrollmentno=models.TextField(max_length=20)
   branch= models.CharField(max_length=5)
