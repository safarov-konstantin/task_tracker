# Generated by Django 5.0.6 on 2024-05-22 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='наименование')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='наименование')),
                ('description', models.TextField(verbose_name='описание')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task_tracker.task', verbose_name='родитель')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task_tracker.status', verbose_name='статус')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
            },
        ),
    ]
