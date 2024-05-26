from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .forms import ProductForm
from .models import Product



def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def book(request):
    return render(request, 'book.html')

def menu(request):
    products = Product.objects.all()
    return render(request, 'menu.html', {'products': products})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book')
        else:
            return render(request, 'book.html', {'form': form})
    else:
        form = ProductForm()
    return render(request, 'book.html', {'form': form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('menu') 
