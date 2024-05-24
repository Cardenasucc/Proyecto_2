from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('menu/', views.menu, name='menu'),
    path('create_product/', views.create_product, name='create_product'),
]
