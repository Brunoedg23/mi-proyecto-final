# Generated by Django 4.1.2 on 2022-10-27 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0002_familiar_fecha_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_blog', models.CharField(max_length=14)),
                ('construido_por', models.CharField(default='', max_length=30)),
                ('titulo_principal', models.CharField(default='', max_length=30)),
                ('subtitulo_principal', models.CharField(default='', max_length=60)),
            ],
        ),
    ]
