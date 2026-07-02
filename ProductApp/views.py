from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from django.db.models import Q



#--------------------------- Home----------------------
def Homepage(request):

    cate=CategoryModel.objects.all()
    filter_cat= request.GET.get('filter_cat')
    Psearch = request.GET.get('Psearch')
    data=ProductModel.objects.all()
    
    if Psearch:
        data=ProductModel.objects.filter(
            Q(name__icontains=Psearch)|
            Q(category__name__icontains = Psearch)|            
            Q(description__icontains = Psearch)
        )
        count=data.count()
        
    elif filter_cat:  
        data=ProductModel.objects.filter(category_id=filter_cat)
        count = data.count() 
    else:
        data=ProductModel.objects.all()
        count=data.count()
    
    
    cont={'data':data, 'count': count, 'cate': cate, 'filter_cat': filter_cat, 'Psearch': Psearch}
    return render(request, 'pages/home.html', cont)



#--------------------------- Authentication----------------------


def Registerpage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register Successful')
            return redirect('login')
    else:
        form=RegisterForm()
    cont={'form': form}
    return render(request, 'auth/register.html', cont)



def LoginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')

            user = authenticate(request, username=username, email=email)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfull')
                return redirect('login')
            else:
                messages.error(request, 'Invalid Credintials')
    else:
        form=LoginForm
    cont={'form': form}
    return render(request, 'auth/login.html', cont)


def LogoutPage(request):
    logout(request)
    messages.info(request, 'Logged out!!')
    return redirect('home')



#--------------------------- Category----------------------

def CategoryPage(request):
    if request.method== 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Added Successfully')
            return redirect('category')
    else:
        form=CategoryForm()
    
    data=CategoryModel.objects.all()
    
    search = request.GET.get('search')

    if search:
        data=CategoryModel.objects.filter(
            Q(name__icontains = search)|
            Q(description__icontains = search)
        )
    else:
        data=CategoryModel.objects.all()

    count = CategoryModel.objects.all().__len__()
    cont={'form':form, "data": data, 'count': count}
    return render(request, 'pages/category.html', cont)



def CategoryEditPage(request,id):
    data=CategoryModel.objects.get(id=id)
    if request.method == 'POST':
        form=CategoryForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated Successfully')
            return redirect('category')
    else:
        form=CategoryForm(instance=data)
    cont={'form':form}
    return render(request, 'pages/editCategory.html', cont)


def DeleteCategorypage(request,id):
    CategoryModel.objects.get(id=id).delete()
    messages.warning(request, 'Category Deleted')
    return redirect('category')




#--------------------------- Product----------------------


def ProductPage(request):
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Added Successfully')
            return redirect('product')
    else:
        form=ProductForm()
    
    filter_cate= request.GET.get('filter_cate')
    if filter_cate:
        data=ProductModel.objects.filter(category_id=filter_cate)
        count= ProductModel.objects.filter(category_id=filter_cate).count()
    else:
        data=ProductModel.objects.all()
        count= ProductModel.objects.all().count()

    cate=CategoryModel.objects.all()    
    cont={'form': form, 'data':data, 'count': count, 'cate':cate, 'filter_cate': filter_cate}
    return render(request, 'pages/product.html', cont)



def editProduct(request,id):
    data=ProductModel.objects.get(id=id)
    if request.method == 'POST':
        form=ProductForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated successfully')
            return redirect('product')
    else:
        form=ProductForm(instance=data)
    cont={'form': form}
    return render(request, 'pages/editProduct.html', cont)

def delProduct(request,id):
    ProductModel.objects.get(id=id).delete()
    messages.warning(request, 'Product Deleted!!')
    return redirect('product')

    





# Create your views here.
