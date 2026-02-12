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
