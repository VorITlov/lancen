from app_profiles.models import *
from app_lancen.models import *
from app_timetable.models import *

from django.urls import reverse
from datetime import datetime


current_datetime = datetime.now()
# Create your models here.



TITLE_CHOICES = [(i,i) for i in range(0,11,5)]

# for i in range(1,31,1):
#     TITLE_CHOICES.append((i,i))

class Journal(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Учитель")
    group = models.ForeignKey(LearingGroup, on_delete=models.CASCADE, verbose_name="Группа")

    def get_absolute_url(self):
        return reverse("journal:view-journal", kwargs={"group": self.group.id, "year": current_datetime.year, "month": current_datetime.month})
    
    def __str__(self):
        return f"Препод: {self.teacher}, группа: {self.group}"

    class Meta:
        verbose_name = "Журнал"
        verbose_name_plural = "Журналы"



class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="ученик")
    lesson_date = models.ForeignKey(TimeTable, on_delete=models.CASCADE, verbose_name="занятие")

    work_on_lesson = models.IntegerField(verbose_name="Работа на уроке", choices=TITLE_CHOICES)
    behavior =models.IntegerField(verbose_name = "Поведение",  choices=TITLE_CHOICES)
    homework = models.IntegerField(verbose_name="Домашнее задание",  choices=TITLE_CHOICES)
    extra = models.IntegerField(verbose_name="EXTRA",  choices=TITLE_CHOICES)
    additional = models.IntegerField(verbose_name="Дополнительные баллы", blank=True, null=True)
    

    class Meta:
            verbose_name = "Оценка"
            verbose_name_plural = "Оценки"


    def __str__(self):
        return f"{self.student} {self.lesson_date}"



class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    lesson_date = models.ForeignKey(TimeTable, on_delete=models.CASCADE, verbose_name="занятие")

    was = models.BooleanField(verbose_name="Был?")

    class Meta:
            verbose_name = "Посещаемость занятия"
            verbose_name_plural = "Посещаемость занятий"

    def __str__(self):

        text = 'НЕ БЫЛ'
        if self.was:
            text = "БЫЛ"
            

        return f"Студент: {self.student} '{self.lesson_date}' числа {text}"
