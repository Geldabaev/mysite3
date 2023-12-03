from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/<int:catid>/', views.category, name='cats'),
    path('post/<int:pk>/', views.post_info, name='post_info'),
    path('post/new/', views.post_new, name='post_new'),
]