from django.urls import path
from .views import CrearCompetenciaView, PruebaCompetenciaView, crearCategoriaView, crear_RA_CategoriaView, crearReglaView, crearAreaEvaluacionView, agregar_CategoriaView, Mostrar_InformacionView
from .views import ModificarCompetenciaView, AsignarJurdoView, InscripcionCompetenciaView, Inscripcion_ExitosaView, Mostrar_InformacionCompetenciaView, GestionarCompetenciasView
from .views import asignar_equipo_logistica, crearEquipoLogisticaView

app_name="competencia"

urlpatterns = [
    path('crear/', CrearCompetenciaView.as_view(), name="crear"),
    path('prueba/', PruebaCompetenciaView.as_view(), name="prueba"),
    path('mostrar-competencias/', Mostrar_InformacionCompetenciaView.as_view(), name="mostrar_competencias"),
    path('gestionar-competencias/', GestionarCompetenciasView.as_view(), name="gestionar_competencias"),
    path('<int:competencia_id>/crear-categoria/', crearCategoriaView.as_view(), name='crear_categoria'), 
    path('<int:competencia_id>/crear-equpo-logistica/', crearEquipoLogisticaView.as_view(), name='crear_equpo_logistica'), 
    path('<int:competencia_id>/inscripcion-exitosa/', Inscripcion_ExitosaView.as_view(), name='incripcion_exitosa'),
    path('<int:competencia_id>/inscripcion/', InscripcionCompetenciaView.as_view(), name='inscripcion_competencia'),
    path('<int:competencia_id>/categoria/<int:categoria_id>/agregar-reglas-areas_evaluacion/', crear_RA_CategoriaView.as_view(), name='crear_RA_categoria'),
    path('<int:competencia_id>/agregar-categorias/', agregar_CategoriaView.as_view(), name='agregar_categorias'),
    path('<int:competencia_id>/mostrar-informacion/', Mostrar_InformacionView.as_view(), name='mostrar_informacion'),
    path('<int:competencia_id>/modificar-competencia/', ModificarCompetenciaView.as_view(), name='modificar_competencia'),
    path('<int:competencia_id>/modificar-competencia/asignar-jurado/', AsignarJurdoView.as_view(), name='asignar_jurado'),
    path('<int:competencia_id>/modificar-competencia/asignar-equpo-logistica/', asignar_equipo_logistica.as_view(), name='asignar_equpo_logistica'),
    path('<int:competencia_id>/categoria/<int:categoria_id>/agregar-regla/', crearReglaView.as_view(), name='crear_regla'),
    path('<int:competencia_id>/categoria/<int:categoria_id>/agregar-area_evaluacion/', crearAreaEvaluacionView.as_view(), name='crear_area_evaluacion'),
]