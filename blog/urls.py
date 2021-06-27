from django.urls import path
from . import views

urlpatterns = [
    # path, view name, url name
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]
# matching URLs coming from mysite.urls will (http://127.0.0.1:8000/) will access the post_list view
