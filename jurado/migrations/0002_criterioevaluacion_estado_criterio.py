# Generated by Django 4.2.6 on 2023-12-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='criterioevaluacion',
            name='estado_criterio',
            field=models.CharField(default='Activo', max_length=100),
        ),
    ]
