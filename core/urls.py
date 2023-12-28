from django.urls import path
from .views import GroceryItemView, GroceryItemDetailView

urlpatterns = [
    path('grocery-items/', GroceryItemView.as_view(), name='grocery-item-list-create'),
    path('grocery-items/<int:pk>/', GroceryItemDetailView.as_view(), name='grocery-item-detail'),
]
