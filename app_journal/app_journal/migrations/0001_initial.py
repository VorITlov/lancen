# Generated by Django 4.1 on 2022-08-19 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_timetable', '__first__'),
        ('app_lancen', '__first__'),
        ('app_profiles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_on_lesson', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name='Работа на уроке')),
                ('behavior', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name='Поведение')),
                ('homework', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name='Домашнее задание')),
                ('extra', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name='EXTRA')),
                ('lesson_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_timetable.timetable', verbose_name='занятие')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_profiles.student', verbose_name='ученик')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_lancen.learinggroup', verbose_name='Группа')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_profiles.teacher', verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журналы',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was', models.BooleanField(verbose_name='Был?')),
                ('lesson_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_timetable.timetable', verbose_name='занятие')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_profiles.student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Посещаемость занятия',
                'verbose_name_plural': 'Посещаемость занятий',
            },
        ),
    ]