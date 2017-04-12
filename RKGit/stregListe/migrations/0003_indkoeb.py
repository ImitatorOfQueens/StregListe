# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stregListe', '0002_vejleder_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indkoeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Dato')),
                ('price', models.IntegerField(verbose_name='Pris')),
                ('event', models.CharField(max_length=300, verbose_name='Anledning')),
                ('descripton', models.CharField(max_length=300, verbose_name='Hvad har du købt?')),
                ('indkoeber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stregListe.Vejleder')),
            ],
        ),
    ]
