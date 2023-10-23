from django.urls import path
from .views import LoginHomeView, exit, registro

app_name="login"

urlpatterns = [
    path('principal/', LoginHomeView.as_view(), name="principal"),
    path('logout/', exit, name='exit'),
    path('registro/', registro, name='registro'),
]
