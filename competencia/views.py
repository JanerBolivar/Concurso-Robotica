from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from .models import Competencia, Categoria, AreaEvaluacion, Regla
from django.urls import reverse

# Create your views here.
class CrearCompetenciaView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'crearCompetencia.html', context)
    
    def post(self, request, *args, **kwargs):
        print("Entro")


class PruebaCompetenciaView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'pruebaCompetencia.html', context)
    
    def post(self, request, *args, **kwargs):
        nombre_competencia = request.POST.get('nombre_competencia')
        descripcion_competencia = request.POST.get('descripcion_competencia')
        lugar_competencia = request.POST.get('lugar_competencia')
        fecha_competencia = request.POST.get('fecha_Competencia')
        fecha_limite_inscripcion = request.POST.get('fecha_limite_inscripcion_Competencia')
        fecha_limite_actualizar = request.POST.get('fecha_limite_actualizar_inscripcion_Competencia')
        
        nueva_competencia = Competencia(
            NombreCompetencia=nombre_competencia,
            DescipcionCompetencia=descripcion_competencia,
            LugarCompetencia=lugar_competencia,
            FechaCompetencia=fecha_competencia,
            FechaLimiteInscripcion=fecha_limite_inscripcion,
            FechaLimiteActualizarDatos=fecha_limite_actualizar,
            EstadoCompetencia = "Creando"
        )
        nueva_competencia.save()
        
        # Guardar banners en la instancia de Competencia
        nueva_competencia.banner1 = request.FILES.get('inputGroupFile01')
        nueva_competencia.banner2 = request.FILES.get('inputGroupFile02')
        nueva_competencia.banner3 = request.FILES.get('inputGroupFile03')
        nueva_competencia.save()

        nueva_competencia = Competencia.objects.latest('id')  # Obtener la última competencia creada
        competencia_id = nueva_competencia.id

        return redirect(reverse('competencia:crear_categoria', kwargs={'competencia_id': competencia_id}))


class crearCategoriaView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        context = {
            'competencia_id': competencia_id,
        }
        return render(request, 'crearCategoria.html', context)
    
    def post(self, request, *args, **kwargs):
        nombre_categoria = request.POST.get('nombre_categoria')
        descripcion_categoria = request.POST.get('descripcion_categoria')

        competencia_id = kwargs['competencia_id']

        competencia = get_object_or_404(Competencia, id=competencia_id)
        
        nueva_categoria = Categoria(
            NombreCategoria=nombre_categoria,
            DescipcionCategoria=descripcion_categoria,
            competencia = competencia
        )
        nueva_categoria.save()

        nueva_categoria = Categoria.objects.latest('id')
        categoria_id = nueva_categoria.id

        # Obtén el ID de la competencia desde los argumentos de la URL
        competencia_id = kwargs['competencia_id']

        # Redirige a crear_RA_CategoriaView con ambos IDs en la URL
        return redirect(reverse('competencia:crear_RA_categoria', kwargs={'competencia_id': competencia_id, 'categoria_id': categoria_id}))


class crear_RA_CategoriaView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')

        categoria = get_object_or_404(Categoria, id=categoria_id)

        context = {
            'competencia_id': competencia_id,
            'categoria_id': categoria_id,
            'nombre_categoria': categoria.NombreCategoria,
            'descripcion_categoria': categoria.DescipcionCategoria,
        }
        return render(request, 'crear_RA_Categoria.html', context)
    
    def post(self, request, *args, **kwargs):
        print("Post de prueba")




class crearReglaView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')

        context = {
            'competencia_id': competencia_id,
            'categoria_id': categoria_id,
        }
        return render(request, 'crearRegla.html', context)
    
    def post(self, request, *args, **kwargs):

        nombre_regla = request.POST.get('nombre_regla')
        descripcion_regla = request.POST.get('descripcion_regla')

        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')

        categoria = get_object_or_404(Categoria, id=categoria_id)
        
        nueva_regla = Regla(
            NombreRegla=nombre_regla,
            DescipcionRegla=descripcion_regla,
            categoria = categoria
        )
        nueva_regla.save()


        return redirect(reverse('competencia:crear_RA_categoria', kwargs={'competencia_id': competencia_id, 'categoria_id': categoria_id}))



class crearAreaEvaluacionView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')

        context = {
            'competencia_id': competencia_id,
            'categoria_id': categoria_id,
        }
        return render(request, 'crearAreaEvaluacion.html', context)
    
    def post(self, request, *args, **kwargs):
        nombre_area_evaluacion = request.POST.get('nombre_area_evaluacion')
        descripcion_area_evaluacion = request.POST.get('descripcion_area_evaluacion')
        porcentaje_area_evaluacion = request.POST.get('porcentaje_area_evaluacion')

        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')

        categoria = get_object_or_404(Categoria, id=categoria_id)
        
        nueva_area_evaluacion = AreaEvaluacion(
            NombreAreaEvaluacion=nombre_area_evaluacion,
            DescipcionAreaEvaluacion=descripcion_area_evaluacion,
            Porcentaje=porcentaje_area_evaluacion,
            categoria = categoria
        )
        nueva_area_evaluacion.save()


        return redirect(reverse('competencia:crear_RA_categoria', kwargs={'competencia_id': competencia_id, 'categoria_id': categoria_id}))

