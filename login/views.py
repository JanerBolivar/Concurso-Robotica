from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

    
class LoginHomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'Home.html', context)

def exit(request):
    logout(request)
    return redirect('home')

def registro(self, request, *args, **kwargs):
    context = {
        'form': CustomUserCreationForm
    }
    return render(request, 'registration/registro.html', context)