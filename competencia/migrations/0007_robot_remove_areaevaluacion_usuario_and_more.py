

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_equipo_tipousuario_participantesequipos_and_more'),
        ('competencia', '0006_areaevaluacion_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreRobot', models.CharField(max_length=60)),
                ('DescripcionRobot', models.CharField(max_length=250)),
                ('imagen_robot', models.CharField(max_length=250, null=True)),
                ('diagrama_conexiones', models.CharField(max_length=250, null=True)),
                ('programacion_robot', models.CharField(max_length=250, null=True)),
                ('EstadoRobot', models.CharField(default='Activo', max_length=60)),
                ('FechaRegistro', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.RemoveField(
            model_name='areaevaluacion',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='competencia',
            name='banner1',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='competencia',
            name='banner2',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='competencia',
            name='banner3',
            field=models.CharField(max_length=250, null=True),
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
                ('imagen_aplicacion', models.CharField(max_length=250, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripcion_categoria', to='competencia.categoria')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripcion_equipo', to='login.equipo')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripcion_robot', to='competencia.robot')),
            ],
        ),
        migrations.CreateModel(
            name='asignacion_jurado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAsignacion', models.DateField(default=datetime.date.today)),
                ('estado_asignacion', models.CharField(default='Activa', max_length=60)),
                ('area_evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AreaEvaluacion', to='competencia.areaevaluacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuario', to='login.usuario')),
            ],
        ),
    ]
