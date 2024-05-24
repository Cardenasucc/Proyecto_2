from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'categories': categories, 'products': products})

def book(request):
    return render(request, 'book.html')

def menu(request):
    return render(request, 'menu.html')

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')  # Redirigimos al usuario a la lista de productos
        else:
            # Si el formulario no es válido, renderizamos el formulario con errores
            return render(request, 'book.html', {'form': form})
    else:
        form = ProductForm()
    return render(request, 'book.html', {'form': form})
