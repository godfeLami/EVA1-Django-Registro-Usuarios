from django.contrib import admin
from django.urls import path
from usuarios import views
from productos import views as productos_views


urlpatterns = [

    # Panel administrativo
    path('admin/', admin.site.urls),

    # Página principal
    path('', views.inicio),

    # Registro de usuarios
    path('registro/', views.registro),

    # Inicio de sesión
    path('login/', views.login),
    
    # Cerrar sesión
    path('logout/', views.logout),

    # Página principal del CRUD
    path('productos/', productos_views.index),

    # Listado de productos
    path('productos/listado/', productos_views.listado),

    # Formulario para registrar
    path('productos/registrar/', productos_views.registrar),

    # Insertar producto
    path('productos/insertar/', productos_views.insertar),

    # Formulario para actualizar
    path('productos/actualizar/<int:id>/', productos_views.actualizar),

    # Modificar producto
    path('productos/modificar/<int:id>/', productos_views.modificar),

    # Eliminar producto
    path('productos/eliminar/<int:id>/', productos_views.eliminar),
]