from django.contrib import admin
from .models import Usuario, TipoUsuario, Equipo, ParticipantesEquipos

# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Equipo)
admin.site.register(ParticipantesEquipos)