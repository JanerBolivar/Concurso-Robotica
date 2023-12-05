from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from core.views import HomeView, AcercaDeView, AccesoNoAutorizadoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('acerca-de', AcercaDeView.as_view(), name="acerca_de"),
    path('acceso-no-autorizado', AccesoNoAutorizadoView.as_view(), name="acceso_no_autorizado"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', include('login.urls', namespace='login')),
    path('competencia/', include('competencia.urls', namespace='competencia')),
    path('jurado/', include('jurado.urls', namespace='jurado')),
    path('logistica/', include('logistica.urls', namespace='logistica')),
]
