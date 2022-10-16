# Generated by Django 4.1 on 2022-08-21 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_journal', '0001_initial'),
        ('app_homework', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='journal_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_journal.journal', verbose_name='журнальный лист'),
        ),
        migrations.AddField(
            model_name='filehomework',
            name='homework',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_homework.homework'),
        ),
    ]