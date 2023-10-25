from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Usuario

    
class LoginHomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'Home.html', context)

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
        nombre1 = request.POST['nombre1']
        nombre2 = request.POST['nombre2']
        apellido1 = request.POST['apellido1']
        apellido2 = request.POST['apellido2']
        #fecha_nacimiento = request.POST['fecha_nacimiento']
        telefono = request.POST['telefono']
        sexo = request.POST['sexo']
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']

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
            #fecha_nacimiento=fecha_nacimiento,
            telefono=telefono,
            sexo=sexo,
            correo=correo,
            contrasena=contrasena,
        )

        # Iniciar sesión al nuevo usuario
        # login(request, usuario)

        # Redireccionar a la página de inicio
        return redirect('home')

def exit(request):
    logout(request)
    return redirect('home')