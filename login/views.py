from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

    
class LoginHomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'Home.html', context)
    
class RegistroView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'registro.html', context)

def exit(request):
    logout(request)
    return redirect('home')