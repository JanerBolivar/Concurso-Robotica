# Generated by Django 4.2.6 on 2023-11-26 21:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_equipo_participantesequipos'),
        ('competencia', '0007_remove_areaevaluacion_usuario_asignacion_jurado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreRobot', models.CharField(max_length=60)),
                ('DescripcionRobot', models.CharField(max_length=250)),
                ('EstadoRobot', models.CharField(default='Activo', max_length=60)),
                ('FechaRegistro', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='inscripcion_competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado_inscripcion', models.CharField(default='Registrado', max_length=60)),
                ('FechaInscripcion', models.DateField(default=datetime.date.today)),
                ('oportunidad1', models.IntegerField(null=True)),
                ('oportunidad2', models.IntegerField(null=True)),
                ('oportunidad3', models.IntegerField(null=True)),
                ('color', models.CharField(default='Sin color', max_length=60)),
                ('imagen_robot', models.CharField(max_length=250, null=True)),
                ('imagen_aplicacion', models.CharField(max_length=250, null=True)),
                ('diagrama_conexiones', models.CharField(max_length=250, null=True)),
                ('codigo_carro', models.CharField(max_length=250, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripcion_categoria', to='competencia.categoria')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripcion_equipo', to='login.equipo')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripcion_robot', to='competencia.robot')),
            ],
        ),
    ]