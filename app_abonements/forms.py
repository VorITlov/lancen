from django import forms

from app_timetable.models import TimeTable
from .models import *
from django.core.exceptions import ValidationError



class SortStudentAbonement(forms.Form):
    """Сортирует занятия в абонементах для студентов"""
    def __init__(self, *args, **kwargs):
        #kwargs.pop('sort_param', None)
        stud = kwargs.pop('stud', None)
        super().__init__(*args, **kwargs)
        choises = [
            [payment_ab.id, f"{payment_ab.abonement.name} ({payment_ab.date_start.day}.{payment_ab.date_start.month}.{payment_ab.date_start.year})" ] for  payment_ab in  PaymentAbonement.objects.filter(student = stud)
        ]
        choises.insert(0,['', '---'])
        self.fields['payment_ab'] = forms.ChoiceField(label="Оплата абонемента", choices=choises, required=False, widget=forms.Select(attrs={"class": "form-control"}))
        

   
class PaymentAbonementForm(forms.ModelForm):
    class Meta:
        model = PaymentAbonement
        fields = "__all__"

    def clean(self):
        if any(self.errors):
            return

        if not search_lesson(self.cleaned_data["student"], self.cleaned_data["date_start"], self.cleaned_data["abonement"]):
            self.add_error(None, "Проверьте что расписание занятий создано верно")


    

def search_lesson(student, date_start, abonement):
    
    lessons = TimeTable.objects.filter(group = student.group, date__gte = date_start)[:int(abonement.amount_lesson)] #gte - больше, lte - меньше

    print(f"{len(lessons)} : {abonement.amount_lesson}")

    if len(lessons) < abonement.amount_lesson:
        return False

    return lessons



def create_lesson(lessons_list, abonement):
    for item in lessons_list:
        payment_lesson = StudentPaymenatLessons(lesson = item, payment_abonement = abonement)
        payment_lesson.save()
        print("У пользователя сохранилось оплаченное занятие")
    return False






