from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    azure_image_url = forms.URLField(label='Azure Blob Storage Image URL', required=True, widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Azure Blob Storage image URL'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'placeholder': 'Price in USD'}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'azure_image_url']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity
