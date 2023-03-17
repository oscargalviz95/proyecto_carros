from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('list_carros/<str:marca>',views.list_carros,name="list_carros")
]

