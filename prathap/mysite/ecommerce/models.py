from django.db import models

# Create your models here.


'''class CustomerPANDetails(models.Model):
    pan_number=models.CharField(max_length=30)
    name_on_pan=models.TextField()
    date_of_birth=models.DateField()


class Customer(models.Model):
    c_name=models.TextField()
    mobile_number=models.CharField(max_length=12)
    email_address=models.EmailField()
    customer_pan_details=models.OneToOneField(CustomerPANDetails,on_delete=models.CASCADE)

    
class Order(models.Model):
    total_value=models.IntegerField()
    date_of_delivery=models.DateField()
    purchase_date=models.DateField()
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    
class Brand(models.Model):
    b_name=models.TextField(unique=True)
    country=models.TextField()
    brand_score=models.IntegerField()
    
class Product(models.Model):
    p_name=models.TextField()
    price=models.IntegerField()
    description=models.TextField()
    Average_rating=models.FloatField()
    order=models.ManyToManyField(Order)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
'''