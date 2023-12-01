from audioop import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from competencia.models import Competencia, Categoria, AreaEvaluacion
from .models import CriterioEvaluacion
from login.models import Usuario
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404

class JuradoCompetenciaView(View):
    def get(self, request, *args, **kwargs):
        competencias = Competencia.objects.all()
        usuario_id = self.kwargs.get('usuario_id')
        usuario = get_object_or_404(Competencia, id=usuario_id)
        context = {
            'usuario': usuario,
            'competencias': competencias,
        }
        return render(request, 'JuradoCompetencia.html', context)

class JuradoCategoriasView(View):
    def get(self, request, *args, **kwargs):
        usuario_id = self.kwargs.get('usuario_id')
        usuario = get_object_or_404(Competencia, id=usuario_id)
        competencia_id = self.kwargs.get('competencia_id')
        competencia = get_object_or_404(Competencia, id=competencia_id)
        categorias = Categoria.objects.filter(competencia=competencia)
        context = {
            'usuario': usuario,
            'competencia': competencia, 
            'categorias': categorias,
        }
        return render(request, 'JuradoCategorias.html', context)
    



class JuradoAreaEvaluacionView(View):
    def get(self, request, *args, **kwargs):
        usuario_id = self.kwargs.get('usuario_id')
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')

        usuario = get_object_or_404(Usuario, id=usuario_id)
        competencia = get_object_or_404(Competencia, id=competencia_id)
        categoria = get_object_or_404(Categoria, id=categoria_id)

        # Obtener las áreas de evaluación de la categoría específica
        areas_evaluacion = AreaEvaluacion.objects.filter(categoria=categoria, usuario=usuario)

        try:
            area_evaluacion = AreaEvaluacion.objects.get(categoria=categoria, usuario=usuario)
        except AreaEvaluacion.DoesNotExist:
            messages.success(request, 'No existe área de evaluación.')
            return redirect('jurado:categorias', usuario_id=usuario_id, competencia_id=competencia_id)

        criterios_evaluacion = CriterioEvaluacion.objects.filter(area_evaluacion=area_evaluacion)

        context = {
            'usuario': usuario,
            'competencia': competencia,
            'categoria': categoria,
            'areas_evaluacion': areas_evaluacion,
            'area_evaluacion': area_evaluacion,
            'criterios_evaluacion': criterios_evaluacion,
        }

        print(usuario)
        print(competencia)
        print(categoria)

        return render(request, 'AreaEvaluacion.html', context)



class AgregarCriterioView(View):
    def get(self, request, *args, **kwargs):
        usuario_id = self.kwargs.get('usuario_id')
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')
        area_evaluacion_id = self.kwargs.get('area_evaluacion_id')

        usuario = get_object_or_404(Competencia, id=usuario_id)
        competencia = get_object_or_404(Competencia, id=competencia_id)
        categoria = get_object_or_404(Categoria, id=categoria_id)
        area_evaluacion = get_object_or_404(AreaEvaluacion, id=area_evaluacion_id)

        criterios_evaluacion = CriterioEvaluacion.objects.filter(area_evaluacion=area_evaluacion)

        context = {
            'usuario': usuario,
            'competencia': competencia,
            'categoria': categoria,
            'area_evaluacion': area_evaluacion,
            'criterios_evaluacion': criterios_evaluacion,
        }
        return render(request, 'AgregarCriterio.html', context)

    def post(self, request, *args, **kwargs):
        usuario_id = self.kwargs.get('usuario_id')
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')
        area_evaluacion_id = self.kwargs.get('area_evaluacion_id')

        Nombre_Criterio = request.POST.get('nombre_Criterio')
        Porcentaje_Criterio = int(request.POST.get('porcentaje_Criterio'))

        usuario = get_object_or_404(Competencia, id=usuario_id)
        competencia = get_object_or_404(Competencia, id=competencia_id)
        categoria = get_object_or_404(Categoria, id=categoria_id)
        area_evaluacion = get_object_or_404(AreaEvaluacion, id=area_evaluacion_id)

        criterios_evaluacion = CriterioEvaluacion.objects.filter(area_evaluacion=area_evaluacion)

        # Verificar si agregar este nuevo criterio excede el 100%
        porcentaje_total = Porcentaje_Criterio + sum(criterio.porcentaje_Criterio for criterio in criterios_evaluacion)
        
        if porcentaje_total > 100:
            messages.error(request, 'La suma de los porcentajes de los criterios no puede exceder el 100%.')
            return redirect('jurado:areas_evaluacion', usuario_id=usuario_id, competencia_id=competencia_id, categoria_id=categoria_id)

        nuevo_Criterio = CriterioEvaluacion(
            nombre_Criterio=Nombre_Criterio,
            porcentaje_Criterio=Porcentaje_Criterio,
            area_evaluacion=area_evaluacion,
        )
        nuevo_Criterio.save()

        usuario_id = usuario.id
        competencia_id = competencia.id
        categoria_id = categoria.id

        return redirect('jurado:areas_evaluacion', usuario_id=usuario_id, competencia_id=competencia_id, categoria_id=categoria_id)

    


class ModificarCriterioView(View):
    template_name = 'ModificarCriterio.html'

    def get(self, request, *args, **kwargs):
        usuario_id = self.kwargs.get('usuario_id')
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')
        area_evaluacion_id = self.kwargs.get('area_evaluacion_id')
        criterio_id = self.kwargs.get('criterio_id')

        usuario = get_object_or_404(Usuario, id=usuario_id)
        competencia = get_object_or_404(Competencia, id=competencia_id)
        categoria = get_object_or_404(Categoria, id=categoria_id)
        area_evaluacion = get_object_or_404(AreaEvaluacion, id=area_evaluacion_id)
        criterio = get_object_or_404(CriterioEvaluacion, id=criterio_id)

        context = {
            'usuario': usuario,
            'competencia': competencia,
            'categoria': categoria,
            'area_evaluacion': area_evaluacion,
            'criterio': criterio,
        }
        return render(request, 'ModificarCriterio.html', context)

    def post(self, request, *args, **kwargs):
        usuario_id = self.kwargs.get('usuario_id')
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')
        criterio_id = self.kwargs.get('criterio_id')

        usuario = get_object_or_404(Usuario, id=usuario_id)
        competencia = get_object_or_404(Competencia, id=competencia_id)
        categoria = get_object_or_404(Categoria, id=categoria_id)
        criterio = get_object_or_404(CriterioEvaluacion, id=criterio_id)

        # Tu lógica para modificar el criterio

        Nombre_Criterio = request.POST.get('nombre_criterio')
        Porcentaje_Criterio = request.POST.get('porcentaje_criterio')

        if not Nombre_Criterio or not Porcentaje_Criterio:
            context = {
                'usuario': usuario,
                'competencia': competencia,
                'categoria': categoria,
                'criterio': criterio,
            }
            return render(request, 'ModificarCriterio.html', context)

        criterio.nombre_Criterio = Nombre_Criterio
        criterio.porcentaje_Criterio = Porcentaje_Criterio
        criterio.save()

        messages.success(request, 'Criterio modificado exitosamente.')

        usuario_id = usuario.id
        competencia_id = competencia.id
        categoria_id = categoria.id

        # Redirige directamente a la vista 'areas_evaluacion'
        return redirect('jurado:areas_evaluacion', usuario_id=usuario_id, competencia_id=competencia_id, categoria_id=categoria_id)
