# Generated by Django 4.2.6 on 2023-11-15 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competencia', '0002_prueba_areaevaluacion_porcentaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaevaluacion',
            name='Porcentaje',
            field=models.IntegerField(),
        ),
    ]