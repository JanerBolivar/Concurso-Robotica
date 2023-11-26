from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from .models import Competencia, Categoria, AreaEvaluacion, Regla, asignacion_jurado
from django.urls import reverse

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from django.http import JsonResponse
from login.models import Usuario, TipoUsuario

from django.contrib import messages

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
        
        # Guardar archivos temporalmente y luego leer su contenido binario
        banner1 = request.FILES.get('inputGroupFile01')
        if banner1:
            file_path = default_storage.save('temp/' + banner1.name, ContentFile(banner1.read()))
            nueva_competencia.banner1 = default_storage.open(file_path).read()

        banner2 = request.FILES.get('inputGroupFile02')
        if banner2:
            file_path = default_storage.save('temp/' + banner2.name, ContentFile(banner2.read()))
            nueva_competencia.banner2 = default_storage.open(file_path).read()

        banner3 = request.FILES.get('inputGroupFile03')
        if banner3:
            file_path = default_storage.save('temp/' + banner3.name, ContentFile(banner3.read()))
            nueva_competencia.banner3 = default_storage.open(file_path).read()
        

        nueva_competencia.save()

        nueva_competencia = Competencia.objects.latest('id')  # Obtener la última competencia creada
        competencia_id = nueva_competencia.id

        return redirect(reverse('competencia:agregar_categorias', kwargs={'competencia_id': competencia_id}))


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


class agregar_CategoriaView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')

        competencia = get_object_or_404(Competencia, id=competencia_id)

        categorias = Categoria.objects.filter(competencia=competencia)

        context = {
            'competencia_id': competencia_id,
            'nombre_competencia': competencia.NombreCompetencia,
            'descripcion_competencia': competencia.DescipcionCompetencia,
            'categorias': categorias,
        }
        return render(request, 'agregar_Categorias.html', context)
    
    def post(self, request, *args, **kwargs):
        print("Post de prueba")





class crear_RA_CategoriaView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        categoria_id = self.kwargs.get('categoria_id')

        categoria = get_object_or_404(Categoria, id=categoria_id)

        reglas = Regla.objects.filter(categoria=categoria)
        areas = AreaEvaluacion.objects.filter(categoria=categoria)

        context = {
            'competencia_id': competencia_id,
            'categoria_id': categoria_id,
            'nombre_categoria': categoria.NombreCategoria,
            'descripcion_categoria': categoria.DescipcionCategoria,
            'reglas': reglas,
            'areas': areas,
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



class Mostrar_InformacionView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')

        competencia = get_object_or_404(Competencia, id=competencia_id)

        categorias = Categoria.objects.filter(competencia=competencia)

        # Obtener las reglas y áreas de evaluación para cada categoría
        for categoria in categorias:
            categoria.reglas = Regla.objects.filter(categoria=categoria)
            categoria.areas_evaluacion = AreaEvaluacion.objects.filter(categoria=categoria)


        context = {
            'competencia_id': competencia_id,
            'competencia': competencia,
            'nombre_competencia': competencia.NombreCompetencia,
            'descripcion_competencia': competencia.DescipcionCompetencia,
            'categorias': categorias,
        }
        return render(request, 'Mostrar_Informacion.html', context)
    
    def post(self, request, *args, **kwargs):
        print("Post de prueba")



class ModificarCompetenciaView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')

        competencia = get_object_or_404(Competencia, id=competencia_id)

        categorias = Categoria.objects.filter(competencia=competencia)

        # Obtener las reglas y áreas de evaluación para cada categoría
        for categoria in categorias:
            categoria.reglas = Regla.objects.filter(categoria=categoria)
            categoria.areas_evaluacion = AreaEvaluacion.objects.filter(categoria=categoria)


        context = {
            'competencia_id': competencia_id,
            'competencia': competencia,
            'nombre_competencia': competencia.NombreCompetencia,
            'descripcion_competencia': competencia.DescipcionCompetencia,
            'categorias': categorias,
        }
        return render(request, 'modificar_Competencia.html', context)
    
    def post(self, request, *args, **kwargs):
        print("Post de prueba")




class AsignarJurdoView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')

        competencia = get_object_or_404(Competencia, id=competencia_id)

        asignaciones = asignacion_jurado.objects.select_related('area_evaluacion__categoria', 'usuario').filter(area_evaluacion__categoria__competencia=competencia)

        # Obtener categorías y áreas de evaluación con asignaciones
        categorias_con_asignaciones = {}
        for asignacion in asignaciones:
            categoria_id = asignacion.area_evaluacion.categoria.id
            area_evaluacion_id = asignacion.area_evaluacion.id

            if categoria_id not in categorias_con_asignaciones:
                categorias_con_asignaciones[categoria_id] = {'categoria': asignacion.area_evaluacion.categoria, 'areas_evaluacion': {}}

            if area_evaluacion_id not in categorias_con_asignaciones[categoria_id]['areas_evaluacion']:
                categorias_con_asignaciones[categoria_id]['areas_evaluacion'][area_evaluacion_id] = {
                    'area_evaluacion': asignacion.area_evaluacion,
                    'asignaciones': [asignacion.usuario],
                }
            else:
                categorias_con_asignaciones[categoria_id]['areas_evaluacion'][area_evaluacion_id]['asignaciones'].append(asignacion.usuario)
        

        categorias = Categoria.objects.filter(competencia=competencia)

        # Obtener las áreas de evaluación para cada categoría
        for categoria in categorias:
            categoria.areas_evaluacion = AreaEvaluacion.objects.filter(categoria=categoria)
        

        
        context = {
            'competencia_id': competencia_id,
            'competencia': competencia,
            'categorias': categorias,
            'categorias_con_asignaciones': categorias_con_asignaciones,
        }
        return render(request, 'AsignarJurado.html', context)
    
    def post(self, request, *args, **kwargs):

        competencia_id = self.kwargs.get('competencia_id')

        competencia = get_object_or_404(Competencia, id=competencia_id)

        categorias = Categoria.objects.filter(competencia=competencia)

        # Obtener las áreas de evaluación para cada categoría
        for categoria in categorias:
            categoria.areas_evaluacion = AreaEvaluacion.objects.filter(categoria=categoria)
        

        categoria_seleccionada = request.POST.get('categoria_seleccionada')
        AreasEvaluacion_seleccionada = request.POST.get('AreasEvaluacion_seleccionada')
        busqueda = request.POST.get('busqueda')

        # Realizar la búsqueda del usuario en la base de datos
        try:
            usuario = Usuario.objects.get(Nombre1=busqueda)  # Modifica esto según tus campos de usuario
            area_evaluacion = get_object_or_404(AreaEvaluacion, id=AreasEvaluacion_seleccionada)
            
            tipo_usuario = get_object_or_404(TipoUsuario, NombreTipoUsuario="Jurado")

            usuario.tipo_usuario = tipo_usuario
            usuario.save()

            nueva_asignacion = asignacion_jurado(
                usuario = usuario,
                area_evaluacion = area_evaluacion,
            )
            nueva_asignacion.save()
            
        except Usuario.DoesNotExist:
            # Si no se encuentra, muestra un mensaje de error utilizando Django messages framework
            messages.error(request, 'El usuario no se encontró en la base de datos.')

        # Devuelve la página, incluyendo los datos y mensajes actualizados
        return redirect(reverse('competencia:asignar_jurado', kwargs={'competencia_id': competencia_id}))


class InscripcionCompetenciaView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')

        competencia = get_object_or_404(Competencia, id=competencia_id)

        categorias = Categoria.objects.filter(competencia=competencia)

        context = {
            'competencia': competencia,
            'categorias': categorias,
        }
        return render(request, 'InscripcionCompetencia.html', context)
    
    def post(self, request, *args, **kwargs):

        competencia_id = self.kwargs.get('competencia_id')
        

        categoria_seleccionada = request.POST.get('categoria_seleccionada')

        nombre_equipo = request.POST.get('nombre_equipo')
        color_equipo = request.POST.get('color_equipo')
        descripcion_equipo = request.POST.get('descripcion_equipo')
        integrante_1 = request.POST.get('integrante_1')
        integrante_2 = request.POST.get('integrante_2')
        integrante_3 = request.POST.get('integrante_3')

        imagen_equipo = request.FILES.get('imagen_equipo')
        video_equipo = request.FILES.get('video_equipo')


        nombre_robot = request.POST.get('nombre_robot')
        descripcion_robot = request.POST.get('descripcion_robot')

        imagen_robot = request.FILES.get('imagen_robot')
        diagrama_conexiones = request.FILES.get('diagrama_conexiones')
        programacion_robot = request.FILES.get('programacion_robot')



        imagen_aplicacion = request.FILES.get('imagen_aplicacion')


        categoria = get_object_or_404(Categoria, id=categoria_seleccionada)

        # Realizar la búsqueda del usuario en la base de datos
        try:
            print("Entro")
            
        except Usuario.DoesNotExist:
            # Si no se encuentra, muestra un mensaje de error utilizando Django messages framework
            messages.error(request, 'El se pudo completar el proceso de inscripción.')

        # Devuelve la página, incluyendo los datos y mensajes actualizados
        return redirect('/')