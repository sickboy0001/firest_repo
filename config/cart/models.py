from django.db import models
from django.conf import settings
from mamazon.models import Product

User=settings.AUTO_USER_MODEL

class cart(models.Model):
  user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
  products = models.ManyToManyField(Product,blank=true)
  total = models.DecimalField(default=0.00 , max_digits=9 , decimal_places=2) #100,000,000.00
  created = models.DateTimeField(auto_now_add=true)
  updated = models.DateTimeField(auto_now=true)
  