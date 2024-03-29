from django.urls import path
from .views import blog_list, blog_create, blog_detail, blog_category

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('create/', blog_create, name='blog_create'),
    path('blog_detail/<str:slug>', blog_detail, name='blog_detail'),
    path('category/<str:slug>', blog_category, name='blog_category'),


]