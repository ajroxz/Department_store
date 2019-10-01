from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fooditems(models.Model):
    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='images')

    body = models.TextField()

    price = models.IntegerField(default=0)

    No_of_items = models.IntegerField(default=0)

class homeutilities(models.Model):
    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='images')

    body = models.TextField()

    price = models.IntegerField(default=0)

    No_of_items = models.IntegerField(default=0)

class beverages(models.Model):
    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='images')

    body = models.TextField()

    price = models.IntegerField(default=0)

    No_of_items = models.IntegerField(default=0)

class grocery(models.Model):
    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='images')

    body = models.TextField()

    price = models.IntegerField(default=0)

    No_of_items = models.IntegerField(default=0)



     

    


