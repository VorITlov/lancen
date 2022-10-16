from django.db import models

from app_journal.models import Journal

# Create your models here.

class Homework(models.Model):
    name = models.CharField(max_length=255, verbose_name='название дз')
    date = models.DateField(verbose_name='дата выдачи дз')
    description = models.TextField(verbose_name='описание дз', blank = True)
    journal_list = models.ForeignKey(Journal, on_delete=models.CASCADE, verbose_name='журнальный лист')

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"

    def __str__(self):
        return self.name

class FileHomework(models.Model):
    file = models.FileField(upload_to= "files_hw/%Y/%m/%d/", verbose_name="Файлы" , blank=True, null=True)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Файлы"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return f"{self.file}"
