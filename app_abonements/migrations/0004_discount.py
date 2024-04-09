# Generated by Django 4.1 on 2024-04-09 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_abonements', '0003_remove_abonement_course_abonement_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField(verbose_name='Значение скидки')),
                ('value', models.CharField(choices=[('руб', 'руб'), ('%', 'процент.')], max_length=255, verbose_name='Величина')),
            ],
            options={
                'verbose_name': 'Значение скидоки',
                'verbose_name_plural': 'Значения скидок',
            },
        ),
    ]
