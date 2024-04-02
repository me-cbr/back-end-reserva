from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=65, unique=True, blank=True, null=True)
    name = models.CharField(max_length=65)
    email = models.EmailField()
    phone = models.CharField(max_length=11, blank=True, null=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username