from django.urls import path
from . import views

app_name = 'grocerylist'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('purchased/<int:id>', views.purchased, name='purchased'),
    path('deleted/<int:id>', views.deleted, name='deleted')
]
