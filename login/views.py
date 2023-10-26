from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import Usuario

    
class LoginHomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'Home.html', context)


class pruebaView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'Login.html', context)
    
    def post(self, request, *args, **kwargs):
        correo = request.POST.get('correo', '')
        contrasena = request.POST.get('contrasena', '')

        # Validar campos vacíos y guardar mensajes de error
        campos_vacios_error = {}
        if not correo:
            campos_vacios_error['correo'] = 'Este campo es obligatorio.'
        if not contrasena:
            campos_vacios_error['contrasena'] = 'Este campo es obligatorio.'
        
        if campos_vacios_error:
            context = {
                'campos_vacios_error': campos_vacios_error,
                'correo': correo,
                'contrasena': contrasena,
            }
            return render(request, 'Login.html', context)

        usuario = Usuario().verificar_login(correo, contrasena)

        if isinstance(usuario, Usuario):
            return render(request, 'Home.html', {'usuario': usuario})
            #return redirect('login:principal')
        else:
            mensaje_error = usuario  # Puede ser "Contraseña incorrecta" o "Cuenta no existe"
            return render(request, 'registro.html', {'error_message': mensaje_error})


# Método para validar si la cuenta ya existe
def existe_cuenta(correo):
    usuario = Usuario.objects.filter(correo=correo).first()
    return usuario is not None


class RegistroView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'correo_error': False,
        }
        return render(request, 'registro.html', context)
    
    def post(self, request, *args, **kwargs):
         # Obtener los datos del formulario
        nombre1 = request.POST.get('nombre1', '')
        nombre2 = request.POST.get('nombre2', '')
        apellido1 = request.POST.get('apellido1', '')
        apellido2 = request.POST.get('apellido2', '')
        telefono = request.POST.get('telefono', '')
        fecha_nacimiento = request.POST.get('fecha_nacimiento', '')
        sexo = request.POST.get('sexo', '')
        correo = request.POST.get('correo', '')
        contrasena = request.POST.get('contrasena', '')
        contrasena_repetida = request.POST.get('contrasena_repetida', '')

        # Validar campos vacíos y guardar mensajes de error
        campos_vacios_error = {}
        if not nombre1:
            campos_vacios_error['nombre1'] = 'Este campo es obligatorio.'
        if not apellido1:
            campos_vacios_error['apellido1'] = 'Este campo es obligatorio.'
        if not apellido2:
            campos_vacios_error['apellido2'] = 'Este campo es obligatorio.'
        if not telefono:
            campos_vacios_error['telefono'] = 'Este campo es obligatorio.'
        if sexo == 'Sexo...':
            campos_vacios_error['sexo'] = 'Este campo es obligatorio.'
        if not correo:
            campos_vacios_error['correo'] = 'Este campo es obligatorio.'
        if not contrasena:
            campos_vacios_error['contrasena'] = 'Este campo es obligatorio.'
        if not contrasena_repetida:
            campos_vacios_error['contrasena_repetida'] = 'Este campo es obligatorio.'

        if campos_vacios_error:
            context = {
                'correo_error': False,
                'campos_vacios_error': campos_vacios_error,
                'nombre1': nombre1,
                'nombre2': nombre2,
                'apellido1': apellido1,
                'apellido2': apellido2,
                'telefono': telefono,
                'sexo': sexo,
                'correo': correo,
                'contrasena': contrasena,
                'contrasena_repetida': contrasena_repetida,
            }
            return render(request, 'registro.html', context)
        

        if contrasena != contrasena_repetida:
            context = {
                'correo_error': False,
                'campos_vacios_error': campos_vacios_error,
                'contrasena_no_coincide': True,
                'nombre1': nombre1,
                'nombre2': nombre2,
                'apellido1': apellido1,
                'apellido2': apellido2,
                'telefono': telefono,
                'sexo': sexo,
                'correo': correo,
                'contrasena': contrasena,
                'contrasena_repetida': contrasena_repetida,
            }
            return render(request, 'registro.html', context)


        # Validar si la cuenta ya existe
        if existe_cuenta(correo):
            usuario_existente = Usuario.objects.get(correo=correo)  # Recupera el usuario existente
            context = {
                'correo_error': True,
                'nombre1': nombre1,
                'nombre2': nombre2,
                'apellido1': apellido1,
                'apellido2': apellido2,
                'telefono': telefono,
                'sexo': sexo,
                'correo': correo,
                'contrasena': contrasena,
            }
            return render(request, 'registro.html', context)
        
        # Crear el nuevo usuario
        usuario = Usuario.objects.create(
            Nombre1=nombre1,
            Nombre2=nombre2,
            Apellido1=apellido1,
            Apellido2=apellido2,
            fecha_nacimiento=fecha_nacimiento,
            telefono=telefono,
            sexo=sexo,
            correo=correo,
            contrasena=contrasena,
        )

        usuario = Usuario().verificar_login(correo, contrasena)

        if isinstance(usuario, Usuario):
            return render(request, 'Home.html', {'usuario': usuario})
            #return redirect('login:principal')
        else:
            mensaje_error = usuario  # Puede ser "Contraseña incorrecta" o "Cuenta no existe"
            return render(request, 'registro.html', {'error_message': mensaje_error})
