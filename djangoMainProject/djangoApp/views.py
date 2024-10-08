
# Create your views here.
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'item_form.html', {'form': form})

def item_update(request, pk):
    item = Item.objects.get(pk=pk)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'item_form.html', {'form': form})

def item_delete(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})

