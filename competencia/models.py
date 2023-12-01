from django.db import models
from django.db.models.fields import CharField, DateField
import datetime 
from login.models import Usuario

# Create your models here.
class Competencia(models.Model):
    NombreCompetencia = CharField(max_length=60)
    DescipcionCompetencia = CharField(max_length=250)
    LugarCompetencia = CharField(max_length=150)
    FechaCompetencia = DateField(default=datetime.date.today)
    FechaLimiteInscripcion = DateField(default=datetime.date.today)
    FechaLimiteActualizarDatos = DateField(default=datetime.date.today)
    EstadoCompetencia = CharField(max_length=60, default="Disponible")
    banner1 = models.BinaryField(null=True, blank=True)
    banner2 = models.BinaryField(null=True, blank=True)
    banner3 = models.BinaryField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.id} {self.NombreCompetencia} {self.EstadoCompetencia}'


class Categoria(models.Model):
    NombreCategoria = CharField(max_length=60)
    DescipcionCategoria = CharField(max_length=250)
    EstadoCategoria = CharField(max_length=60, default="Disponible")
    competencia = models.ForeignKey('Competencia', on_delete=models.CASCADE, related_name='Categoria')

    def __str__(self) -> str:
        return f'{self.id} {self.NombreCategoria} {self.EstadoCategoria}'


class AreaEvaluacion(models.Model):
    NombreAreaEvaluacion = CharField(max_length=60)
    DescipcionAreaEvaluacion = CharField(max_length=250)
    EstadoAreaEvaluacion = CharField(max_length=60, default="Disponible")
    Porcentaje = models.IntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='AreaEvaluacion')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Usuario')

    def __str__(self) -> str:
        return f'{self.id} {self.NombreAreaEvaluacion} {self.EstadoAreaEvaluacion}'


class Regla(models.Model):
    NombreRegla = CharField(max_length=60)
    DescipcionRegla = CharField(max_length=250)
    EstadoRegla = CharField(max_length=60, default="Disponible")
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='Regla')

    def __str__(self) -> str:
        return f'{self.id} {self.NombreRegla} {self.EstadoRegla}'