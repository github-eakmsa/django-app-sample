
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('items/create/', views.create, name="create"),
    path('items/list/', views.list, name="list"),
]
