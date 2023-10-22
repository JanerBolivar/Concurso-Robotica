from django.urls import path
from .views import LoginListView

app_name="login"

urlpatterns = [
    path('', LoginListView.as_view(), name="home"),
]
