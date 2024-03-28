from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class FoodType(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    title = models.CharField(max_length=65)
    city = models.CharField(max_length=65, default='')
    neighborhood = models.CharField(max_length=65, default='')
    description = models.CharField(max_length=255)
    opening_hours = models.TimeField()
    closing_hours = models.TimeField()
    img_restaurant = models.ImageField(upload_to='restaurant/cover/img', blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    food_type = models.ForeignKey(FoodType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Classification(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    classification = models.IntegerField(default='')
    comment = models.TextField(default='')