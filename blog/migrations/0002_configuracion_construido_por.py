# Generated by Django 4.1.2 on 2022-10-27 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='construido_por',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
