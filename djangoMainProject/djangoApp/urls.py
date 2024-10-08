from django.urls import path
from .views import item_list, item_create, item_update, item_delete

urlpatterns = [
    path('', item_list, name='item_list'),
    path('item/new/', item_create, name='item_create'),
    path('item/<int:pk>/edit/', item_update, name='item_update'),
    path('item/<int:pk>/delete/', item_delete, name='item_delete'),
]
