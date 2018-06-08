from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_temp/', views.add_temp, name='temp'),
    path('view_json/', views.view_json, name='json')
]