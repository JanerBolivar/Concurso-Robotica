from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class JuradoHomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'IndexHome.html', context)
    
class JuradoCompetenciaView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'JuradoCompetencia.html', context)