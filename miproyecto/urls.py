from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    # Acceso al panel administrativo de Django
    path('admin/', admin.site.urls),
    # Página principal
    path('', views.inicio),
    # Registro de nuevos usuarios
    path('registro/', views.registro),
    # Inicio de sesión
    path('login/', views.login),
]
