from django.urls import path
from .views import CrearCompetenciaView, PruebaCompetenciaView, crearCategoriaView, crear_RA_CategoriaView, crearReglaView, crearAreaEvaluacionView, agregar_CategoriaView, Mostrar_InformacionView
from .views import ModificarCompetenciaView, AsignarJurdoView, buscar_personas

app_name="competencia"

urlpatterns = [
    path('crear/', CrearCompetenciaView.as_view(), name="crear"),
    path('prueba/', PruebaCompetenciaView.as_view(), name="prueba"),
    path('buscar_personas/', buscar_personas, name="buscar_personas"),
    path('<int:competencia_id>/crear-categoria/', crearCategoriaView.as_view(), name='crear_categoria'),
    path('<int:competencia_id>/categoria/<int:categoria_id>/agregar-reglas-areas_evaluacion/', crear_RA_CategoriaView.as_view(), name='crear_RA_categoria'),
    path('<int:competencia_id>/agregar-categorias/', agregar_CategoriaView.as_view(), name='agregar_categorias'),
    path('<int:competencia_id>/mostrar-informacion/', Mostrar_InformacionView.as_view(), name='mostrar_informacion'),
    path('<int:competencia_id>/modificar-competencia/', ModificarCompetenciaView.as_view(), name='modificar_competencia'),
    path('<int:competencia_id>/modificar-competencia/asignar-jurado', AsignarJurdoView.as_view(), name='asignar_jurado'),
    path('<int:competencia_id>/categoria/<int:categoria_id>/agregar-regla/', crearReglaView.as_view(), name='crear_regla'),
    path('<int:competencia_id>/categoria/<int:categoria_id>/agregar-area_evaluacion/', crearAreaEvaluacionView.as_view(), name='crear_area_evaluacion'),
]