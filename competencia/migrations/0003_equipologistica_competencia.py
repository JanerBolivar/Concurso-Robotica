# Generated by Django 4.2.6 on 2023-12-03 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competencia', '0002_equipologistica_participacion_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipologistica',
            name='competencia',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Comptencia_EquipoLogistica', to='competencia.competencia'),
            preserve_default=False,
        ),
    ]
