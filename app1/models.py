from django.db import models
from django.contrib.auth.models import User

class product_available(models.Model):
    pro_name=models.CharField(max_length=255,null=True)
    pro_price=models.IntegerField(null=True)
    pro_description=models.CharField(max_length=300,null=True)
    pro_image=models.ImageField(upload_to='images/',blank=True)


class user_Model(models.Model):
    user_birth=models.DateField(null=True)
    user_address=models.CharField(max_length=255,null=True)
    user_number=models.IntegerField(null=True)
    user_gender=models.CharField(max_length=250,null=True)
    user_district=models.CharField(max_length=250,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
class cart_item(models.Model):
    item=models.ForeignKey(product_available,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True,null=True)
    quantity=models.IntegerField(null=True)
    price=models.FloatField(null=True)
    is_ordered=models.BooleanField(default=False,null=True)
    
class cartModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    items=models.ManyToManyField(cart_item)

# Create your models here.