from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('animal/add/', views.animal_create, name='animal_add'),
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('animal/<int:animal_pk>/vaccine/add/', views.vaccine_create, name='vaccine_add'),
]
