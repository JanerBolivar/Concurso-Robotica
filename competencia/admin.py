from django.contrib import admin
from .models import Competencia, Categoria, AreaEvaluacion, Regla, asignacion_jurado

# Register your models here.
admin.site.register(Competencia)
admin.site.register(Categoria)
admin.site.register(AreaEvaluacion)
admin.site.register(Regla)
admin.site.register(asignacion_jurado)