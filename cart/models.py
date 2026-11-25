from django.db import models
from django.contrib.auth.models import User
from products.models import products

class cart(models.Model):
    cartno=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
class cartitems(models.Model):
    cartitemno=models.AutoField(primary_key=True)
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    
