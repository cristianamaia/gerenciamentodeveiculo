# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marcadoveiculo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('marca', models.CharField(help_text='Ex. Nissan, HondaFiat', max_length=20, verbose_name='MarcaDoVeiculo')),
            ],
            options={
                'ordering': ('marca',),
                'verbose_name': 'Marca de Veiculo',
                'verbose_name_plural': 'Marca De Veiculos',
            },
        ),
        migrations.CreateModel(
            name='Tipodeveiculo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('tipo', models.CharField(help_text='Ex. Carro ou Moto', max_length=20, verbose_name='Tipo de veiculo')),
            ],
            options={
                'ordering': ('tipo',),
                'verbose_name': 'Tipo de Veiculo',
                'verbose_name_plural': 'Tipo De Veiculos',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('placa', models.CharField(max_length=8, verbose_name='Placa')),
                ('cor', models.CharField(max_length=10, verbose_name='Cor')),
                ('marca', models.ForeignKey(to='app_veiculo.Marcadoveiculo')),
                ('tipo', models.ForeignKey(to='app_veiculo.Tipodeveiculo')),
            ],
            options={
                'ordering': ('tipo', 'marca', 'modelo'),
                'verbose_name': 'Veiculo',
                'verbose_name_plural': 'Veiculos',
            },
        ),
    ]
