from django.urls import path
from .views import CompetenciasDisponiblesView, EquiposDisponiblesView, TareasDisponiblesView

app_name="logistica"

urlpatterns = [
    path('competencias-disponibles', CompetenciasDisponiblesView.as_view(), name="competencias_disponibles"),
    path('competencia/<int:competencia_id>/equipos-disponibles/', EquiposDisponiblesView.as_view(), name="equipos_disponibles"),
    path('competencia/<int:competencia_id>/equipo/<int:equipo_id>/tareas-disponibles', TareasDisponiblesView.as_view(), name="tareas-disponibles"),
]
