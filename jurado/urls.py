from django.urls import path
from .views import JuradoCompetenciaView, JuradoCategoriasView, JuradoAreaEvaluacionView, AgregarCriterioView,ModificarCriterioView

app_name = "jurado"

urlpatterns = [
    path('usuario/<int:usuario_id>/competencias/', JuradoCompetenciaView.as_view(), name="competencias"),
    path('usuario/<int:usuario_id>/categoria/<int:competencia_id>/', JuradoCategoriasView.as_view(), name='categorias'),
    path('usuario/<int:usuario_id>/competencia/<int:competencia_id>/categoria/<int:categoria_id>/areas_evaluacion/', JuradoAreaEvaluacionView.as_view(), name='areas_evaluacion'),
    path('usuario/<int:usuario_id>/competencia/<int:competencia_id>/categoria/<int:categoria_id>/<int:area_evaluacion_id>/', AgregarCriterioView.as_view(), name='agregar_criterio'),
    path('usuario/<int:usuario_id>/competencia/<int:competencia_id>/categoria/<int:categoria_id>/<int:area_evaluacion_id>/modificar_criterio/<int:criterio_id>/', ModificarCriterioView.as_view(), name='modificar_criterio'),
]
