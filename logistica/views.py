from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from competencia.models import Competencia, Participacion_Equipo, EquipoLogistica, Tarea_EquipoLogistica
from login.models import Usuario, Equipo, TipoUsuario

# Create your views here.
class CompetenciasDisponiblesView(View):
    def get(self, request, *args, **kwargs):
        competencias = Competencia.objects.filter(EstadoCompetencia="Disponible")

        usuario_id = request.COOKIES.get('usuario_id')

        if usuario_id:
            usuario = Usuario.objects.get(id=usuario_id)
            
            if usuario.tipo_usuario.NombreTipoUsuario == "Logistica":
                context = {
                    'usuario_id': usuario_id,
                    'usuario': usuario,
                    'competencias': competencias,
                }
                return render(request, 'Competencias_Disponibles.html', context)
            else:
                return redirect('acceso_no_autorizado')
        else:
            return redirect('login:prueba')


class EquiposDisponiblesView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        competencia = get_object_or_404(Competencia, id=competencia_id)

        equipos = EquipoLogistica.objects.filter(competencia=competencia, EstadoEquipoLogistica="Disponible")

        usuario_id = request.COOKIES.get('usuario_id')

        if usuario_id:
            usuario = Usuario.objects.get(id=usuario_id)
            
            if usuario.tipo_usuario.NombreTipoUsuario == "Logistica":
                context = {
                    'usuario_id': usuario_id,
                    'usuario': usuario,
                    'competencia': competencia,
                    'equipos': equipos,
                }
                return render(request, 'Equipos_Disponibles.html', context)
            else:
                return redirect('acceso_no_autorizado')
        else:
            return redirect('login:prueba')


class TareasDisponiblesView(View):
    def get(self, request, *args, **kwargs):
        competencia_id = self.kwargs.get('competencia_id')
        equipo_id = self.kwargs.get('equipo_id')


        competencia = get_object_or_404(Competencia, id=competencia_id)
        equipo = get_object_or_404(EquipoLogistica, id=equipo_id)

        tareas_equipo = Tarea_EquipoLogistica.objects.filter(equipo_logistica=equipo)

        equipos_logistica_asignados = []
        
        asignaciones = Participacion_Equipo.objects.filter(equipo_logistica=equipo)
        integrantes_asignados = [asignacion.usuario for asignacion in asignaciones]

        if integrantes_asignados:  # Si hay integrantes asignados, añadir a la lista
            equipos_logistica_asignados.append({
                'equipo': equipo,
                'integrantes': integrantes_asignados,
            })

        usuario_id = request.COOKIES.get('usuario_id')

        if usuario_id:
            usuario = Usuario.objects.get(id=usuario_id)
            
            if usuario.tipo_usuario.NombreTipoUsuario == "Logistica":
                context = {
                    'usuario_id': usuario_id,
                    'usuario': usuario,
                    'competencia': competencia,
                    'equipo': equipo,
                    'tareas_equipo': tareas_equipo,
                    'equipos_logistica_asignados': equipos_logistica_asignados,
                }
                return render(request, 'Tareas_Disponibles.html', context)
            else:
                return redirect('acceso_no_autorizado')
        else:
            return redirect('login:prueba')