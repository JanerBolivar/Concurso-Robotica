from django.urls import path
from .views import JuradoCompetenciaView, JuradoCategoriasView, JuradoAreaEvaluacionView, AgregarCriterioView, ModificarCriterioView,EquiposView,EliminarCriterioView,EvaluarEquipoView

app_name = "jurado"

urlpatterns = [
    path('competencias-disponibles/', JuradoCompetenciaView.as_view(), name="competencias_disponibles"),
    path('competencia/<int:competencia_id>/', JuradoCategoriasView.as_view(), name='categorias_disponibles'),
    path('competencia/<int:competencia_id>/categoria/<int:categoria_id>/areas_evaluacion/', JuradoAreaEvaluacionView.as_view(), name='areas_evaluacion'),
    path('competencia/<int:competencia_id>/categoria/<int:categoria_id>/<int:area_evaluacion_id>/', AgregarCriterioView.as_view(), name='agregar_criterio'),
    path('competencia/<int:competencia_id>/categoria/<int:categoria_id>/<int:area_evaluacion_id>/modificar_criterio/<int:criterio_id>/', ModificarCriterioView.as_view(), name='modificar_criterio'),
    path('eliminar_criterio/<int:competencia_id>/<int:categoria_id>/<int:area_evaluacion_id>/<int:criterio_id>/', EliminarCriterioView.as_view(), name='eliminar_criterio'),
    path('competencia/<int:competencia_id>/equipos/<int:categoria_id>/', EquiposView.as_view(), name="equipos"),
    path('competencia/<int:competencia_id>/equipos/<int:categoria_id>/evaluar_equipo/<int:equipo_id>/', EvaluarEquipoView.as_view(), name='evaluar_equipo'),

]
