import django
from django.db import models
from django.db.models.fields import CharField, DateField, EmailField
import datetime


class TipoUsuario(models.Model):
    NombreTipoUsuario = CharField(max_length=60)
    DescipcionTipoUsuario = CharField(max_length=250)
    EstadoTipoUsuario = CharField(max_length=60, default="Disponible")

    def _str_(self) -> str:
        return f'{self.id} {self.NombreTipoUsuario} {self.EstadoTipoUsuario}'


class Usuario(models.Model):
    Nombre1 = CharField(max_length=60)
    Nombre2 = CharField(max_length=60, blank=True)
    Apellido1 = CharField(max_length=60)
    Apellido2 = CharField(max_length=60)
    fecha_nacimiento = DateField(default=datetime.date.today)
    sexo = CharField(max_length=50)
    telefono = CharField(max_length=10)
    correo = EmailField(unique=True, max_length=255, blank=False)
    contrasena = CharField(
        max_length=128,
        blank=False,
        null=False,
        validators=[
            django.core.validators.MinLengthValidator(8),
        ],
    )
    tipo_usuario = models.ForeignKey('TipoUsuario', on_delete=models.CASCADE, related_name='usuarios')

    def _str_(self):
        return f'{self.Nombre1} {self.Apellido1}'


class Equipo(models.Model):
    NombreEquipo = CharField(max_length=60)
    DescipcionEquipo = CharField(max_length=250)
    imagen_equipo = CharField(max_length=250, null=True)
    video_equipo = CharField(max_length=250, null=True)
    EstadoEquipo = CharField(max_length=60, default="Activo")
    fecha_registro = DateField(default=datetime.date.today)

    def _str_(self):
        return f'{self.NombreEquipo} {"Fecha registro: "} {self.fecha_registro}'


class ParticipantesEquipos(models.Model):
    Estado_ParticipanteEquipo = CharField(max_length=60, default="Activo")
    fecha_ParticipanteEquipo = DateField(default=datetime.date.today)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='ParticipantesUsuarios')
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE, related_name='ParticipantesEquipos')

    def _str_(self):
        return f'{"Estado participacion: "} {self.Estado_ParticipanteEquipo}'
