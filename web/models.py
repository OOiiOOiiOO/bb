from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Karjha (models.Model):
    text = models.CharField(max_length=255)
    date  = models.DateField()
    amount = models.IntegerField()
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} -    {}-{}".format(self.text, self.amount, self.date)
    
class Daramad (models.Model):
    text = models.CharField(max_length=255)
    date  = models.DateField()
    amount = models.IntegerField()
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{} -    {}-{}".format(self.text, self.amount, self.date)