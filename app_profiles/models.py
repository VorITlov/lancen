from django.db import models
from django.contrib.auth.models import User

from app_lancen.models import *



# Create your models here.

class Teacher(User):
    experience = models.CharField(max_length=255, verbose_name="Опыт работы")
    photo = models.ImageField(upload_to = get_file_path, verbose_name="Фотография", blank = True)
    description = models.TextField(verbose_name="Описание сотрудника")
    #published = models.BooleanField(verbose_name="Публиковать на главной странице сайта?", blank=True)

    # def get_absolute_url(self):
    #     return reverse("view_teacher", kwargs={"id": self.pk})
    
    
    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(User):
    photo = models.ImageField(upload_to = get_file_path, verbose_name="Фотография", blank = True)
    group = models.ForeignKey(LearingGroup, on_delete=models.CASCADE, verbose_name="Группа")


    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"


    def __str__(self):
        return f"{self.first_name} {self.last_name}, Группа: {self.group}"
    