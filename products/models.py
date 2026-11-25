from django.db import models

# Create your models here.
class category(models.Model):
    catid=models.IntegerField(primary_key=True)
    catname=models.CharField(max_length=20)
    def __str__(self):
        return(self.catname)
class products(models.Model):
    prdno=models.IntegerField(primary_key=True)
    prdname=models.CharField(max_length=20)
    price=models.IntegerField()
    quantity=models.IntegerField()
    category=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    picture=models.ImageField(upload_to='images/',null=True)
    
