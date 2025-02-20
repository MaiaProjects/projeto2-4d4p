# Generated by Django 5.1.6 on 2025-02-19 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_consultas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visualizacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.consultas')),
            ],
        ),
    ]
