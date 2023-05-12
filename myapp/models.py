from django.db import models
from unicodedata import name
# Create your models here.

class My(models.Model):
    name = models.CharField(max_length =100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    
    
# command
# python3 manage.py