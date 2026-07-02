from django.urls import path
from .views import *

urlpatterns = [
    path('', Homepage, name='home'),

    path('register/', Registerpage, name='register'),
    path('login/', LoginPage, name='login'),
    path('logout/', LogoutPage, name='logout'),


    path('category/', CategoryPage, name='category'),
    path('editCategory/<str:id>/', CategoryEditPage, name='editCategory'),
    path('delCategory/<str:id>/', DeleteCategorypage, name='delCategory'),


    path('product/', ProductPage, name='product'),
    path('editProduct/<str:id>/', editProduct, name='editProduct'),
    path('delProduct/<str:id>/', delProduct, name='delProduct'),
]