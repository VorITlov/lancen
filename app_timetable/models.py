from django.db import models
from app_lancen.models import *
from django.urls import reverse

# Create your models here.


class TimeTable(models.Model):
    group = models.ForeignKey(LearingGroup, on_delete=models.CASCADE, verbose_name='Для какой группы')
    date = models.DateField(verbose_name='Дата проведения занятия')
    comment = models.TextField(verbose_name='Комментарий (в случае необходимости)', blank=True)
    canceled = models.BooleanField(verbose_name="Отмена", blank=True, default=False)

    class Meta:
        verbose_name = "Расписание занятия группы"
        verbose_name_plural = "Расписание занятий групп"

    
    def __str__(self):
        return f"В {self.group} группе {self.date} числа" 
