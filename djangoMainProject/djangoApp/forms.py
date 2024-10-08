from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nombre', 'descripcion', 'precio']


'''
# Agregando Items Manualmente
nuevo_item = Item(nombre='Laptop', descripcion='Laptop MSI', precio=1000.50)
nuevo_item.save()

'''

