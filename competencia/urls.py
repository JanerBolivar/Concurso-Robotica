from django.urls import path
from .views import CrearCompetenciaView, PruebaCompetenciaView, crearCategoriaView, crear_RA_CategoriaView, crearReglaView, crearAreaEvaluacionView

app_name="competencia"

urlpatterns = [
    path('crear/', CrearCompetenciaView.as_view(), name="crear"),
    path('prueba/', PruebaCompetenciaView.as_view(), name="prueba"),
    path('<int:competencia_id>/crear-categoria/', crearCategoriaView.as_view(), name='crear_categoria'),
    path('<int:competencia_id>/categoria/<int:categoria_id>/agregar-reglas-areas_evaluacion/', crear_RA_CategoriaView.as_view(), name='crear_RA_categoria'),
    path('<int:competencia_id>/categoria/<int:categoria_id>/agregar-regla/', crearReglaView.as_view(), name='crear_regla'),
    path('<int:competencia_id>/categoria/<int:categoria_id>/agregar-area_evaluacion/', crearAreaEvaluacionView.as_view(), name='crear_area_evaluacion'),
]