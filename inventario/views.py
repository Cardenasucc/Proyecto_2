from django.shortcuts import render
from .models import Category, Product

def home(request):
    # Obtener todas las categorías y todos los productos
    categories = Category.objects.all()
    products = Product.objects.all()
    # Pasar las categorías y los productos como contexto a la plantilla
    return render(request,'index.html', {'categories': categories, 'products': products})

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def book(request):
    return render(request, 'book.html')

def menu(request):
    return render(request, 'menu.html')