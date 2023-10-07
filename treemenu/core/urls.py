
from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<str:blog_id>/', views.blog_detail, name='blog_detail'),
    path('', views.home, name='home'),
]