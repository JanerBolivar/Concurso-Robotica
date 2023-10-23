from django.shortcuts import render
from django.views.generic import View


class LoginListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'Login.html', context)
    
class LoginHomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'Home.html', context)