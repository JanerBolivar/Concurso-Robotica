from django.contrib import admin
from .models import Competencia, Categoria, AreaEvaluacion, Regla, asignacion_jurado, Robot, inscripcion_competencia, EquipoLogistica

# Register your models here.
admin.site.register(Competencia)
admin.site.register(Categoria)
admin.site.register(AreaEvaluacion)
admin.site.register(Regla)
admin.site.register(asignacion_jurado)
admin.site.register(Robot)
admin.site.register(inscripcion_competencia)
admin.site.register(EquipoLogistica)