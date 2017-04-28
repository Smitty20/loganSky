from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Order(models.Model):
    service = models.CharField(max_length=200)
    order_date = models.DateTimeField('date ordered')
    fulfilled = models.BooleanField(default = False)
    
    def __str__(self):
        return self.service
    
# Create your models here.
