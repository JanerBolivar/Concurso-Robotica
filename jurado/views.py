from audioop import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from competencia.models import Competencia, Categoria, AreaEvaluacion, asignacion_jurado
from .models import CriterioEvaluacion
from login.models import Usuario
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404

class JuradoCompetenciaView(View):
    def get(self, request, *args, **kwargs):
        competencias = Competencia.objects.filter(EstadoCompetencia="Disponible")

        usuario_id = request.COOKIES.get('usuario_id')

        if usuario_id:
            usuario = Usuario.objects.get(id=usuario_id)
            
            if usuario.tipo_usuario.NombreTipoUsuario == "Jurado":
                context = {
                    'usuario_id': usuario_id,
                    'usuario': usuario,
                    'competencias': competencias,
                }
                return render(request, 'JuradoCompetencia.html', context)
            else:
                return redirect('acceso_no_autorizado')
        else:
            return redirect('login:prueba')

class JuradoCategoriasView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        competencia = get_object_or_404(Competencia, id=competencia_id)
        categorias = Categoria.objects.filter(competencia=competencia)

        usuario_id = request.COOKIES.get('usuario_id')

        if usuario_id:
            usuario = Usuario.objects.get(id=usuario_id)
            
            if usuario.tipo_usuario.NombreTipoUsuario == "Jurado":
                context = {
                    'usuario_id': usuario_id,
                    'usuario': usuario,
                    'competencia': competencia, 
                    'categorias': categorias,
                }
                return render(request, 'JuradoCategorias.html', context)
            else:
                return redirect('acceso_no_autorizado')
        else:
            return redirect('login:prueba')
    
    



class JuradoAreaEvaluacionView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')

        competencia = get_object_or_404(Competencia, id=competencia_id)
        categoria = get_object_or_404(Categoria, id=categoria_id)

        usuario_id = request.COOKIES.get('usuario_id')

        area_asignada = 0

        if usuario_id:
            usuario = Usuario.objects.get(id=usuario_id)

            areas_asignadas = asignacion_jurado.objects.filter(
                usuario=usuario, 
                area_evaluacion__categoria=categoria,
                estado_asignacion="Activa"
            )

            if areas_asignadas.exists():
                area_evaluacion = areas_asignadas.first().area_evaluacion
                
                criterios_evaluacion = CriterioEvaluacion.objects.filter(area_evaluacion=area_evaluacion, estado_criterio="Activo")

                if usuario.tipo_usuario.NombreTipoUsuario == "Jurado":
                    context = {
                        'usuario_id': usuario_id,
                        'usuario': usuario,
                        'competencia': competencia,
                        'categoria': categoria,
                        'area_evaluacion': area_evaluacion,
                        'criterios_evaluacion': criterios_evaluacion,
                    }
                    return render(request, 'AreaEvaluacion.html', context)
                else:
                    return redirect('acceso_no_autorizado')
            else:
                return redirect('acceso_no_autorizado')
        else:
            return redirect('login:prueba')



class AgregarCriterioView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')
        area_evaluacion_id = self.kwargs.get('area_evaluacion_id')

        competencia = get_object_or_404(Competencia, id=competencia_id)
        categoria = get_object_or_404(Categoria, id=categoria_id)
        area_evaluacion = get_object_or_404(AreaEvaluacion, id=area_evaluacion_id)

        criterios_evaluacion = CriterioEvaluacion.objects.filter(area_evaluacion=area_evaluacion, estado_criterio="Activo")

        usuario_id = request.COOKIES.get('usuario_id')

        if usuario_id:
            usuario = Usuario.objects.get(id=usuario_id)
            
            if usuario.tipo_usuario.NombreTipoUsuario == "Jurado":
                context = {
                    'usuario_id': usuario_id,
                    'usuario': usuario,
                    'competencia': competencia,
                    'categoria': categoria,
                    'area_evaluacion': area_evaluacion,
                    'criterios_evaluacion': criterios_evaluacion,
                }
                return render(request, 'AgregarCriterio.html', context)
            else:
                return redirect('acceso_no_autorizado')
        else:
            return redirect('login:prueba')

    def post(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')
        area_evaluacion_id = self.kwargs.get('area_evaluacion_id')

        Nombre_Criterio = request.POST.get('nombre_Criterio')
        Porcentaje_Criterio = int(request.POST.get('porcentaje_Criterio'))

        competencia = get_object_or_404(Competencia, id=competencia_id)
        categoria = get_object_or_404(Categoria, id=categoria_id)
        area_evaluacion = get_object_or_404(AreaEvaluacion, id=area_evaluacion_id)

        criterios_evaluacion = CriterioEvaluacion.objects.filter(area_evaluacion=area_evaluacion, estado_criterio="Activo")

        # Verificar si agregar este nuevo criterio excede el 100%
        porcentaje_total = Porcentaje_Criterio + sum(criterio.porcentaje_Criterio for criterio in criterios_evaluacion)
        
        if porcentaje_total > 100:
            messages.error(request, 'La suma de los porcentajes de los criterios no puede exceder el 100%.')
            return redirect('jurado:areas_evaluacion', competencia_id=competencia_id, categoria_id=categoria_id)

        nuevo_Criterio = CriterioEvaluacion(
            nombre_Criterio=Nombre_Criterio,
            porcentaje_Criterio=Porcentaje_Criterio,
            area_evaluacion=area_evaluacion,
        )
        nuevo_Criterio.save()

        competencia_id = competencia.id
        categoria_id = categoria.id

        return redirect('jurado:areas_evaluacion', competencia_id=competencia_id, categoria_id=categoria_id)

    


class ModificarCriterioView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')
        area_evaluacion_id = self.kwargs.get('area_evaluacion_id')
        criterio_id = self.kwargs.get('criterio_id')

        competencia = get_object_or_404(Competencia, id=competencia_id)
        categoria = get_object_or_404(Categoria, id=categoria_id)
        area_evaluacion = get_object_or_404(AreaEvaluacion, id=area_evaluacion_id)
        criterio = get_object_or_404(CriterioEvaluacion, id=criterio_id)

        usuario_id = request.COOKIES.get('usuario_id')

        if usuario_id:
            usuario = Usuario.objects.get(id=usuario_id)
            
            if usuario.tipo_usuario.NombreTipoUsuario == "Jurado":
                context = {
                    'usuario_id': usuario_id,
                    'usuario': usuario,
                    'competencia': competencia,
                    'categoria': categoria,
                    'area_evaluacion': area_evaluacion,
                    'criterio': criterio,
                }
                return render(request, 'ModificarCriterio.html', context)
            else:
                return redirect('acceso_no_autorizado')
        else:
            return redirect('login:prueba')

    def post(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')
        criterio_id = self.kwargs.get('criterio_id')

        competencia = get_object_or_404(Competencia, id=competencia_id)
        categoria = get_object_or_404(Categoria, id=categoria_id)
        criterio = get_object_or_404(CriterioEvaluacion, id=criterio_id)

        # Tu lógica para modificar el criterio

        Nombre_Criterio = request.POST.get('nombre_criterio')
        Porcentaje_Criterio = request.POST.get('porcentaje_criterio')

        usuario_id = request.COOKIES.get('usuario_id')

        if not Nombre_Criterio or not Porcentaje_Criterio:
            if usuario_id:
                usuario = Usuario.objects.get(id=usuario_id)
                
                if usuario.tipo_usuario.NombreTipoUsuario == "Jurado":
                    context = {
                        'usuario_id': usuario_id,
                        'usuario': usuario,
                        'competencia': competencia,
                        'categoria': categoria,
                        'criterio': criterio,
                    }
                    return render(request, 'ModificarCriterio.html', context)
                else:
                    return redirect('acceso_no_autorizado')
            else:
                return redirect('login:prueba')

        criterio.nombre_Criterio = Nombre_Criterio
        criterio.porcentaje_Criterio = Porcentaje_Criterio
        criterio.save()

        competencia_id = competencia.id
        categoria_id = categoria.id

        # Redirige directamente a la vista 'areas_evaluacion'
        return redirect('jurado:areas_evaluacion', competencia_id=competencia_id, categoria_id=categoria_id)
