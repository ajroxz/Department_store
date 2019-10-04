from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)

    pub_date = models.DateTimeField(auto_now_add=True)

    exp_date = models.DateTimeField()

    image = models.ImageField(upload_to='images')
    
    body = models.TextField()

    price = models.IntegerField(default=1)

    No_of_items = models.IntegerField(default=1)

    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

   

    



     

    


