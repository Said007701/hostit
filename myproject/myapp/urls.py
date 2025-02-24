from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('price/', views.price, name='price'),
    path('service/', views.service, name='service'),
    path('list/', views.list, name='list'),
    path('create/', views.index1_create, name='create'),
    path('update/<int:id>/', views.index1_update, name='update'),
    path('delete/<int:id>/', views.index1_delete, name='delete'),
    
]