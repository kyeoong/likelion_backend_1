# models.py

from django.db import models

class Order(models.Model):
    menu_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    comment = models.TextField()





"""
from django.db import models
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "<Name : {}, ID : {} >".format(self.name,self.id)
"""