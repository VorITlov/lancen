# Generated by Django 4.1 on 2024-04-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_journal', '0003_alter_mark_behavior_alter_mark_extra_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='additional',
            field=models.IntegerField(blank=True, null=True, verbose_name='Дополнительные баллы'),
        ),
    ]