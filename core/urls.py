from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from core.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', include('login.urls', namespace='login')),
]
