# Generated by Django 4.1.2 on 2022-11-04 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0005_alter_vivienda_tipo_casa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivienda',
            name='descripcion',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
