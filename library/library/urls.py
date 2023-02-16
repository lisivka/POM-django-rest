"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from author.views import AuthorViewSet
from book.views import BookViewSet
from authentication.views import UserViewSet, UserOrdersListView, UserAllOrdersListView  # , UserListView
from order.views import OrderViewSet

router = DefaultRouter()
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'book', BookViewSet, basename='book')
router.register(r'user', UserViewSet, basename='user')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    path('author/', include('author.urls')),
    path('authors/', include('author.urls')),
    path('book/', include('book.urls')),
    path('books/', include('book.urls')),
    path('order/', include('order.urls')),
    path('orders/', include('order.urls')),
    path('auth/', include('authentication.urls')),
    path('users/', include('authentication.urls')),
    path('authentication/', include('authentication.urls')),

    # for API
    path('api/v1/', include(router.urls)),
    path('api/v1/user/<user_id>/order/', UserAllOrdersListView.as_view()),
    path('api/v1/user/<user_id>/order/<order_id>', UserOrdersListView.as_view()),

]
