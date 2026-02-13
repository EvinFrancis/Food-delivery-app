from django.db import models

# Create your models here.
class FoodType(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    foodimage=models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name
class restaurantDb(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    contact_number=models.CharField(max_length=20)
    restaurant_image=models.ImageField(upload_to='restaurant_images/')

    def __str__(self):
        return self.name

class dishesDb(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    food_type=models.CharField(max_length=100)
    restaurant=models.CharField(max_length=100)
    dish_image=models.ImageField(upload_to='dish_images/')
    veg_nonveg=models.CharField(max_length=10,default='veg')

    def __str__(self):
        return self.name
    
    # service database 
class serviceDb(models.Model):
    ServiceName=models.CharField(max_length=100)
    Description=models.TextField()
    ServiceImage=models.ImageField(upload_to="services")
    def __str__(self):
        return self.ServiceName
    
class contactDb(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    subject=models.CharField(max_length=200,default='No Subject')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name