import django
from django.db import models
from django.db.models.fields import CharField, DateField, EmailField 
import datetime


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

    def __str__(self) -> str:
        return f'{self.Nombre1} {self.Apellido1}'