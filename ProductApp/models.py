from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    def __str__(self):
        return self.name
    

class CategoryModel(models.Model):
    name = models.CharField(max_length=120, null=True)
    description = models.TextField(null=True)
    created_at= models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name



class ProductModel(models.Model):
    name=models.CharField(max_length=120, null=True)
    description = models.TextField(null=True)
    category= models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    price= models.FloatField(null=True, default=0)
    stock_quantity= models.IntegerField(null=True, default=0)
    created_at= models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name




# Create your models here.
