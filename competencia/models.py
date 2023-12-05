from django.db import models
from django.db.models.fields import CharField, DateField
import datetime

from django.forms import IntegerField
from login.models import Usuario, Equipo

# Create your models here.
class Competencia(models.Model):
    NombreCompetencia = CharField(max_length=60)
    DescipcionCompetencia = CharField(max_length=250)
    LugarCompetencia = CharField(max_length=150)
    FechaCompetencia = DateField(default=datetime.date.today)
    FechaLimiteInscripcion = DateField(default=datetime.date.today)
    FechaLimiteActualizarDatos = DateField(default=datetime.date.today)
    EstadoCompetencia = CharField(max_length=60, default="Disponible")
    banner1 = CharField(max_length=250, null=True)
    banner2 = CharField(max_length=250, null=True)
    banner3 = CharField(max_length=250, null=True)

    def _str_(self) -> str:
        return f'{self.id} {self.NombreCompetencia} {self.EstadoCompetencia}'


class Categoria(models.Model):
    NombreCategoria = CharField(max_length=60)
    DescipcionCategoria = CharField(max_length=250)
    EstadoCategoria = CharField(max_length=60, default="Disponible")
    competencia = models.ForeignKey('Competencia', on_delete=models.CASCADE, related_name='Categoria')

    def _str_(self) -> str:
        return f'{self.id} {self.NombreCategoria} {self.EstadoCategoria}'


class AreaEvaluacion(models.Model):
    NombreAreaEvaluacion = CharField(max_length=60)
    DescipcionAreaEvaluacion = CharField(max_length=250)
    EstadoAreaEvaluacion = CharField(max_length=60, default="Disponible")
    Porcentaje = models.IntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='AreaEvaluacion')

    def _str_(self) -> str:
        return f'{self.id} {self.NombreAreaEvaluacion} {self.EstadoAreaEvaluacion}'


class Regla(models.Model):
    NombreRegla = CharField(max_length=60)
    DescipcionRegla = CharField(max_length=250)
    EstadoRegla = CharField(max_length=60, default="Disponible")
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='Regla')

    def _str_(self) -> str:
        return f'{self.id} {self.NombreRegla} {self.EstadoRegla}'


class EquipoLogistica(models.Model):
    NombreEquipoLogistica = CharField(max_length=60)
    DescipcionEquipoLogistica = CharField(max_length=450)
    EstadoEquipoLogistica = CharField(max_length=60, default="Disponible")
    competencia = models.ForeignKey('Competencia', on_delete=models.CASCADE, related_name='Comptencia_EquipoLogistica')

    def _str_(self) -> str:
        return f'{self.id} {self.NombreEquipoLogistica} {self.EstadoEquipoLogistica}'


class Participacion_Equipo(models.Model):
    fechaParticipacion = DateField(default=datetime.date.today)
    estado_participacion = CharField(max_length=60, default="Activa")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='UsuarioEquipoLogistica')
    equipo_logistica = models.ForeignKey('EquipoLogistica', on_delete=models.CASCADE, related_name='ParticipacionEquipoLogistica')

    def _str_(self) -> str:
        return f'{"Asignacion de Jurado: "} {self.usuario.Nombre1} {"  Área Evaluacion: "} {self.equipo_logistica.NombreEquipoLogistica}'



class asignacion_jurado(models.Model):
    fechaAsignacion = DateField(default=datetime.date.today)
    estado_asignacion = CharField(max_length=60, default="Activa")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Usuario')
    area_evaluacion = models.ForeignKey('AreaEvaluacion', on_delete=models.CASCADE, related_name='AreaEvaluacion')

    def _str_(self) -> str:
        return f'{"Asignacion de Jurado: "} {self.usuario.Nombre1} {"  Área Evaluacion: "} {self.area_evaluacion.NombreAreaEvaluacion}'


class Robot(models.Model):
    NombreRobot = CharField(max_length=60)
    DescripcionRobot = CharField(max_length=250)
    imagen_robot = CharField(max_length=250, null=True)
    diagrama_conexiones = CharField(max_length=250, null=True)
    programacion_robot = CharField(max_length=250, null=True)
    EstadoRobot = CharField(max_length=60, default="Activo")
    FechaRegistro = DateField(default=datetime.date.today)

    def _str_(self) -> str:
        return f'{"Nombre: "} {self.NombreRobot}'


class inscripcion_competencia(models.Model):
    Estado_inscripcion = CharField(max_length=60, default="Registrado")
    FechaInscripcion = DateField(default=datetime.date.today)
    oportunidad1 = models.FloatField(null=True)
    oportunidad2 = models.FloatField(null=True)
    oportunidad3 = models.FloatField(null=True)
    resultado_total = models.FloatField(null=True)
    color = CharField(max_length=60, default="Sin color")
    imagen_aplicacion = CharField(max_length=250, null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='inscripcion_categoria')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='inscripcion_equipo')
    robot = models.ForeignKey('Robot', on_delete=models.CASCADE, related_name='inscripcion_robot')

    def __str__(self) -> str:
        return f'{"Estado inscripcion: "} {self.Estado_inscripcion} {self.equipo.NombreEquipo}'


class Tarea_EquipoLogistica(models.Model):
    NombreTarea = CharField(max_length=60)
    DescipcionTarea = CharField(max_length=250)
    EstadoTarea = CharField(max_length=60, default="Disponible")
    equipo_logistica = models.ForeignKey('EquipoLogistica', on_delete=models.CASCADE, related_name='TareasEquipoLogistica')

    def __str__(self) -> str:
        return f'{self.NombreTarea} {self.DescipcionTarea}'