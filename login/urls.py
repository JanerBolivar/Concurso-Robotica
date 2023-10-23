from django.urls import path
from .views import LoginHomeView, LoginListView

app_name="login"

urlpatterns = [
    path('', LoginListView.as_view(), name="home"),
    path('principal/', LoginHomeView.as_view(), name="principal"),
]
