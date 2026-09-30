from django.http import request
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.hashers import make_password, check_password

# Vista principal del sistema
def inicio(request):
    return render(request, 'usuarios/inicio.html')

# Vista encargada de registrar nuevos usuarios
def registro(request):
    # Verificamos si el formulario fue enviado mediante POST
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        
        # Comprobamos que ambas contraseñas sean iguales
        if password != password_confirm:
            return render(request, 'usuarios/registro.html', {
                'error': 'Las contraseñas no coinciden.'
            })
            
        # La contraseña debe tener como mínimo 8 caracteres
        if len(password) < 8:
            return render(request, 'usuarios/registro.html', {
                'error': 'La contraseña debe tener al menos 8 caracteres.'
            })
            
        # La contraseña debe contener al menos una letra mayúscula
        if not any(caracter.isupper() for caracter in password):
            return render(request, 'usuarios/registro.html', {
                'error': 'La contraseña debe contener al menos una letra mayúscula.'
            })
            
        # La contraseña debe contener al menos un número
        if not any(caracter.isdigit() for caracter in password):
            return render(request, 'usuarios/registro.html', {
                'error': 'La contraseña debe contener al menos un número.'
            })
            
        # Verificamos que el nombre de usuario no esté registrado
        if Usuario.objects.filter(username=username).exists():
            return render(request, 'usuarios/registro.html', {
                'error': 'El nombre de usuario ya existe.'
            })
            
        # Verificamos que el correo no esté registrado
        if Usuario.objects.filter(email=email).exists():
            return render(request, 'usuarios/registro.html', {
                'error': 'El correo electrónico ya está registrado.'
            })
            
        # Guardamos la contraseña utilizando hash en lugar de texto plano
        Usuario.objects.create(
            username=username, 
            email=email, 
            password=make_password(password)
        )

        return render(request, 'usuarios/inicio.html', {
            'mensaje': 'Registro exitoso. Bienvenido, ' + username
        })
        
    return render(request, 'usuarios/registro.html')
    
# Vista encargada de autenticar a los usuarios
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Buscamos al usuario por su nombre de usuario
            usuario = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            # No revelamos si el usuario existe o no
            return render(request, 'usuarios/login.html', {
                'error': 'Usuario o contraseña incorrectos.'
            })
            
        # Verificamos si la cuenta ya se encuentra bloqueada
        
        if usuario.bloqueado:
            return render(request, 'usuarios/login.html', {
                'error': 'Clave bloqueada. Ha superado el máximo de intentos permitidos.'
            })

        # Comparamos la contraseña ingresada con el hash almacenado
        
        if not check_password(password, usuario.password):
            # Aumentamos el contador de intentos incorrectos
            usuario.intentos += 1
            
            # Al llegar al tercer intento se bloquea la cuenta
            
            if usuario.intentos >= 3:
                usuario.bloqueado = True
                usuario.save()
                
                return render(request, 'usuarios/login.html', {
                    'error': 'Clave bloqueada. Ha superado el máximo de intentos permitidos.'
                })
                
            # Guardamos la cantidad actual de intentos
            usuario.save()
            
            return render(request, 'usuarios/login.html', {
                'error': 'Usuario o contraseña incorrectos.'
            })
            
        # Si el login es correcto, reiniciamos el contador de intentos
        
        usuario.intentos = 0
        usuario.save()

        # Guardamos el usuario en la sesión
        request.session['usuario_id'] = usuario.id
        
        # Enviamos el nombre de usuario a la plantilla de bienvenida
        return render(request, 'usuarios/bienvenida.html', {
            'username': usuario.username
        })

    return render(request, 'usuarios/login.html')

# Cerrar sesión
def logout(request):

    # Eliminamos la información de la sesión
    request.session.flush()

    return redirect('/login/')