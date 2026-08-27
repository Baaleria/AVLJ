from django.urls import path
from . import views # . significa que importa views desde la ruta actual

urlpatterns = [
    path('v1/', views.Inicio),
    path('v3/', views.Inicio)
]