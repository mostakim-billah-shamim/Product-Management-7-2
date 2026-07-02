from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email']


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))


class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'

