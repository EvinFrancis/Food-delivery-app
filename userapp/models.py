from django.db import models

# Create your models here.
class userDb(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.username


class cartdb(models.Model):
    username=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    quantity=models.IntegerField(max_length=100)
    price=models.IntegerField(max_length=100)
    total_price=models.IntegerField(max_length=100)
    product_image=models.ImageField(upload_to='cart_images/' ,null=True,blank=True)

    def __str__(self):
        return self.username


class chechoutdb(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    totalprice=models.IntegerField(max_length=100)

    