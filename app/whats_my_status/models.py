from django.db import models

# Create your models here.
class AmountSpent(models.Model):
    property = models.CharField(null=True,blank=True,max_length=100)
    updatedOn = models.DateTimeField(auto_now_add=True)
    amountSpentOn = models.CharField(null=True,blank=True,max_length=100)
    amount = models.IntegerField()

class TimeSpent(models.Model):
    property = models.CharField(null=True,blank=True,max_length=100)
    updatedOn = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField()
    timeSpentOn = models.CharField(null=True,blank=True,max_length=100)