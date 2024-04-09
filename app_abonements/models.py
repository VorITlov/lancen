from django.db import models

from app_lancen.models import TrainingProgramm , get_file_path
from app_profiles.models import Student
from app_timetable.models import TimeTable

from django.urls.base import reverse
# Create your models here.


discount_CHOICES = (
    ('руб', 'руб'),
    ('%','процент.')
)


class Abonement(models.Model):

    name = models.CharField(verbose_name="Название абонемента", max_length=255)
    amount_lesson = models.IntegerField(verbose_name="Кол-во занятий")
    price = models.IntegerField(verbose_name="Стоимость абонемента (руб.)")
    duration = models.CharField(verbose_name="Продолжительность 1 занятия", max_length=255)
    description  = models.TextField(verbose_name="Описание")
    course = models.ManyToManyField(TrainingProgramm, verbose_name="К какому курсу", related_name='abonement_courses')
    photo = models.ImageField(verbose_name="Фото", upload_to=get_file_path)


    def __str__(self):
        return f"{self.name} {self.price}руб."

    # def get_absolute_url(self):
    #     return reverse("abonement_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"
    

class PaymentAbonement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Какой студент")
    abonement = models.ForeignKey(Abonement , on_delete=models.CASCADE, verbose_name="Какой абонемент")
    date_start = models.DateField(verbose_name="Дата старта абонемента")
    date_payment = models.DateField(verbose_name="Дата оплаты абонемента абонемента")
    discount = models.IntegerField(verbose_name="Скидка в рублях (если есть)" , blank=True, null=True)

    def __str__(self):
        return f"{self.student.last_name} {self.student.first_name.upper()[0]}. => {self.date_start}  {self.abonement.name}"

    class Meta:
        verbose_name = "Оплата абонемента"
        verbose_name_plural = "Оплаты абонементов"


class StudentPaymenatLessons(models.Model):

    lesson = models.ForeignKey(TimeTable, on_delete=models.CASCADE, verbose_name="К какому уроку ")
    payment_abonement = models.ForeignKey(PaymentAbonement, on_delete=models.CASCADE, verbose_name="К какой оплате студента")

    class Meta:
        verbose_name = "Оплаченное занятие пользователя"
        verbose_name_plural = "Оплаченные занятия пользователя"


    def __str__(self):
        return f"{self.lesson.date}: {self.payment_abonement.student}"


class Discount(models.Model):
    discount = models.IntegerField("Значение скидки")
    value = models.CharField("Величина", choices=discount_CHOICES, max_length=255)
    class Meta:
        verbose_name = "Значение скидоки"
        verbose_name_plural = "Значения скидок"
    def __str__(self):
        return f"{self.discount} {self.value}"