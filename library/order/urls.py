from django.urls import path
from .views import index, orders, order_item
from . import views

urlpatterns = [
    path('', orders),
    path('index', index),
    path('orders', orders),
    path('orders/<int:order_id>/', views.order_item, name='order_item'),
    path('orders/delete/<int:pk>/', views.delete_order, name='delete_order'),
    path('orders/close/<int:pk>/', views.close_order, name='close_order'),

    path('orders/create', views.create_order, name='create_order'),
    # path('edit/<int:order_id>', views.edit_order, name='edit_order'),
    path('add_order/<int:order_id>/', views.add_order, name='add_order'),

]
