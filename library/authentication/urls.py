from django.urls import path
from . import views
from .views import  UserOrdersListView #UserListView,

urlpatterns = [
    path('', views.users_new, name='users'),
    path('register/', views.create_user_new, name='register'),
    path('update/<int:user_id>', views.create_user_new, name='update_user'),
    path('login/', views.login_, name='loginnew'),
    path("logout/", views.logout_request, name='logout'),
    path('users/<int:user_id>/', views.user_item, name='user_item'),
    path('delete/<int:user_id>', views.delete_user, name='delete_user'),
    path('reset', views.reset_passwd, name='reset_password'),

]
