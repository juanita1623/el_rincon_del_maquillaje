# Generated by Django 5.1.3 on 2024-11-17 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('autor', models.CharField(default='Anonimo', max_length=20)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
