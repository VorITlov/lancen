# Generated by Django 4.1 on 2022-08-19 22:42

import app_lancen.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LearingGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название группы')),
                ('level', models.CharField(max_length=255, verbose_name='Уровень')),
                ('description', models.TextField(verbose_name='Описание (программа обучения и пр.)')),
            ],
            options={
                'verbose_name': 'Учебная группа',
                'verbose_name_plural': 'Учебные группы',
                'db_table': 'learning_group',
            },
        ),
        migrations.CreateModel(
            name='TrainingProgramm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to=app_lancen.models.get_file_path, verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Программа обучения',
                'verbose_name_plural': 'Программы обучения',
            },
        ),
    ]