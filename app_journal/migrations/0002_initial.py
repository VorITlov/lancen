# Generated by Django 4.1 on 2022-08-21 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_timetable', '0001_initial'),
        ('app_profiles', '0001_initial'),
        ('app_journal', '0001_initial'),
        ('app_lancen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_profiles.student', verbose_name='ученик'),
        ),
        migrations.AddField(
            model_name='journal',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_lancen.learinggroup', verbose_name='Группа'),
        ),
        migrations.AddField(
            model_name='journal',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_profiles.teacher', verbose_name='Учитель'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='lesson_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_timetable.timetable', verbose_name='занятие'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_profiles.student', verbose_name='Студент'),
        ),
    ]
