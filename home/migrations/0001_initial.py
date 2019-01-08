# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-01-08 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(blank=True, max_length=50, null=True)),
                ('event', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TechProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('email', models.EmailField(blank=True, max_length=60, null=True)),
                ('mobileNumber', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(related_name='members', to='home.TechProfile'),
        ),
        migrations.AddField(
            model_name='team',
            name='teamLeader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamLeader', to='home.TechProfile'),
        ),
    ]
