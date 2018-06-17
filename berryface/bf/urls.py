from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert_temp/', views.insert_temp, name='insert_temp'),
    path('view_json/', views.view_json, name="view_json"),
    path('clear_db/', views.clear_db, name="clear_db"),
    path('add_sensor/', views.add_sensor, name="add_sensor"),
    path('add_entry/', views.add_entry, name="add_entry"),
    path('add_roles/', views.add_roles, name="add_roles"),
    path('add_user/', views.add_user, name="add_user"),
    path('view_token/', views.view_token, name="view_token"),
]