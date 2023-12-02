from django.views.generic import View
from django.shortcuts import render
from login.models import Usuario

class HomeView(View):
    def get(self, request, *args, **kwargs):
        usuario_id = request.COOKIES.get('usuario_id')

        if not usuario_id:
            context = {
                'usuario_id': usuario_id
            }
            return render(request, 'index.html', context)
        else:
            usuario = Usuario.objects.get(id=usuario_id)
            context = {
                'usuario_id': usuario_id,
                'usuario': usuario,
            }
            return render(request, 'index.html', context)


class AcercaDeView(View):
    def get(self, request, *args, **kwargs):
        usuario_id = request.COOKIES.get('usuario_id')

        if not usuario_id:
            context = {
                'usuario_id': usuario_id
            }
            return render(request, 'acerca_de.html', context)
        else:
            usuario = Usuario.objects.get(id=usuario_id)
            context = {
                'usuario_id': usuario_id,
                'usuario': usuario,
            }
            return render(request, 'acerca_de.html', context)


class AccesoNoAutorizadoView(View):
    def get(self, request, *args, **kwargs):

        usuario_id = request.COOKIES.get('usuario_id')

        if not usuario_id:
            context = {
                'usuario_id': usuario_id
            }
            return render(request, 'Acceso_no_autorizado.html', context)
        else:
            usuario = Usuario.objects.get(id=usuario_id)
            context = {
                'usuario_id': usuario_id,
                'usuario': usuario,
            }
            return render(request, 'Acceso_no_autorizado.html', context)