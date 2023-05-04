from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('agregarPerro/', views.agregarPerro),
    path('agregarGato/', views.agregarGato),
    path('agregarPajaro/', views.agregarPajaro),
    path('buscar/', views.buscar),
]
