from django.db import models
from django.db.models import *
from django.db import *

# Create your models here.

class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    price_per_unit = models.FloatField()
    
class Order(models.Model):
    order_no = models.UUIDField()
    total_price = models.FloatField()
    products = models.ManyToManyField(Product, through = 'OrderProducts')
    
class OrderProducts(models.Model):
    order = models.ForeignKey(
        'Order', on_delete = models.CASCADE, related_name = 'order_products'
        )
    product = models.ForeignKey(
        'Product', on_delete = models.CASCADE, related_name = 'order_products'
        )
    quantity = models.IntegerField(default=1)
        
