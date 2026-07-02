from django.contrib import admin
from .models import *

admin.site.register([UserModel, CategoryModel, ProductModel])

# Register your models here.
