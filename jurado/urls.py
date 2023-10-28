from django.urls import path
from .views import JuradoHomeView, JuradoCompetenciaView

app_name="jurado"

urlpatterns = [
    path('', JuradoHomeView.as_view(), name="home"),
    path('competancias/', JuradoCompetenciaView.as_view(), name="competancias"),
]