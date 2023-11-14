from django.urls import path
from .views import CrearCompetenciaView

app_name="competencia"

urlpatterns = [
    path('crear/', CrearCompetenciaView.as_view(), name="crear"),
]