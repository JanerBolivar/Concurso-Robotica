from django.db import models
from django.forms import CharField
from competencia.models import AreaEvaluacion  # Ajusta el nombre del archivo y el modelo según sea necesario

class CriterioEvaluacion(models.Model):
    nombre_Criterio = models.CharField(max_length=100)
    porcentaje_Criterio = models.FloatField()
    area_evaluacion = models.ForeignKey(AreaEvaluacion, on_delete=models.CASCADE, related_name='CriterioEvaluacion')