from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # matching URLs coming from mysite.urls will (http://127.0.0.1:8000/) will access the post_list view
]