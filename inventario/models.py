from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_products(self):
        return self.products.all()

    class Meta:
        db_table = 'categories'  # Nombre personalizado para la tabla de categorías

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', to_field='name', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'  # Nombre personalizado para la tabla de productos
