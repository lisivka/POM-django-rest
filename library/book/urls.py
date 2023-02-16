from django.urls import path

from .views import index, books, book_item, books_list
from . import views

urlpatterns = [
    # path('', books),
    path('', books, name='books'),
    path('index', index),
    path('books', books),
    path('books_list', books_list, name='books_list'),
    path('books/<int:book_id>/', views.book_item, name='book_item'),

    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/create', views.create_book, name='create_book'),

    path('books/add_book/<int:book_id>/', views.add_book, name='add_book'),

]
