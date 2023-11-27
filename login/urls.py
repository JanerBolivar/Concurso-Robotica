from django.urls import path
from .views import LoginHomeView, pruebaView, RegistroView

app_name="login"

urlpatterns = [
    path('principal/<int:usuario_id>', LoginHomeView.as_view(), name="principal"),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('prueba/', pruebaView.as_view(), name='prueba'),
]
