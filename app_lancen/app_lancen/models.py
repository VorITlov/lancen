from django.db import models
import uuid
import os
from django.urls.base import reverse
# Create your models here.



def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('uploads/photos', filename)

class LearingGroup(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=255)
    level = models.CharField(verbose_name='Уровень', max_length=255)
    description = models.TextField(verbose_name="Описание (программа обучения и пр.)")


    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"
        db_table = "learning_group"

    def __str__(self):
        return self.name


class TrainingProgramm(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to = get_file_path, verbose_name="Фото")

    class Meta:
        verbose_name = "Программа обучения"
        verbose_name_plural = "Программы обучения"

    def get_absolute_url(self):
        return reverse("lancen:course_view", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.name

    

