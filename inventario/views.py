from django.shortcuts import render
from .models import Category, Product

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request,'index.html', {'categories': categories, 'products': products})

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def book(request):
    return render(request, 'book.html')

def menu(request):
    return render(request, 'menu.html')