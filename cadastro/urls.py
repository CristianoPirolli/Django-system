from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('animal/add/', views.animal_create, name='animal_add'),
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('animal/<int:pk>/editar/', views.animal_edit, name='animal_edit'),
    path('animal/<int:pk>/excluir/', views.animal_delete, name='animal_delete'),
    path('animal/<int:animal_pk>/vaccine/add/', views.vaccine_create, name='vaccine_add'),
    path('animal/<int:animal_pk>/vaccine/<int:pk>/editar/', views.vaccine_edit, name='vaccine_edit'),
    path('animal/<int:animal_pk>/vaccine/<int:pk>/excluir/', views.vaccine_delete, name='vaccine_delete'),
]
