from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto


# Página principal del CRUD
def index(request):

    # Verificamos que el usuario haya iniciado sesión
    if 'usuario_id' not in request.session:
        return redirect('/login/')

    return render(request, 'productos/index.html')


# Mostrar todos los productos
def listado(request):

    # Verificamos que el usuario haya iniciado sesión
    if 'usuario_id' not in request.session:
        return redirect('/login/')

    productos = Producto.objects.all()

    return render(request, 'productos/listado.html', {
        'productos': productos
    })


# Mostrar formulario de registro
def registrar(request):

    # Verificamos que el usuario haya iniciado sesión
    if 'usuario_id' not in request.session:
        return redirect('/login/')

    return render(request, 'productos/form_registrar.html')


# Insertar un nuevo producto
def insertar(request):

    # Verificamos que el usuario haya iniciado sesión
    if 'usuario_id' not in request.session:
        return redirect('/login/')

    if request.method == 'POST':

        nombre = request.POST['txtnom']
        marca = request.POST['cbomar']
        precio = request.POST['txtpre']

        Producto.objects.create(
            nombre=nombre,
            marca=marca,
            precio=precio
        )

        return redirect('/productos/listado/')

    return redirect('/productos/registrar/')


# Mostrar formulario de actualización
def actualizar(request, id):

    # Verificamos que el usuario haya iniciado sesión
    if 'usuario_id' not in request.session:
        return redirect('/login/')

    producto = get_object_or_404(Producto, id=id)

    return render(request, 'productos/form_actualizar.html', {
        'producto': producto
    })


# Modificar un producto
def modificar(request, id):

    # Verificamos que el usuario haya iniciado sesión
    if 'usuario_id' not in request.session:
        return redirect('/login/')

    if request.method == 'POST':

        producto = get_object_or_404(Producto, id=id)

        producto.nombre = request.POST['txtnom']
        producto.marca = request.POST['cbomar']
        producto.precio = request.POST['txtpre']

        producto.save()

        return redirect('/productos/listado/')

    return redirect('/productos/listado/')


# Eliminar un producto
def eliminar(request, id):

    # Verificamos que el usuario haya iniciado sesión
    if 'usuario_id' not in request.session:
        return redirect('/login/')

    producto = get_object_or_404(Producto, id=id)

    producto.delete()

    return redirect('/productos/listado/')