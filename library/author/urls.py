from django.urls import path, include


from . import views



urlpatterns = [
    # path('api/', include(router.urls)),
    path('', views.author_list),
    # path('', views.authors), # Стара версія не на формах  Джанго
    path('authors/<int:author_id>/', views.author_item, name='author_item'),
    path('create/', views.create_author_new, name='create_author_new'),
    path('update/<int:author_id>/', views.create_author_new, name='author_update'),
    path('delete/<int:author_id>/', views.delete, name='author_delete'),

    path('authors/delete/<int:pk>/', views.delete_author, name='delete_author'),

]
