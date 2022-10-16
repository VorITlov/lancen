from django.db.models import Count

from .forms import ContactForm, RecallForm

from .models import LearingGroup
from app_profiles.models import *

from django.core.exceptions import PermissionDenied

menu = [
    {'title' : "Главная", 'link' : 'lancen:index'},
    {'title' : "Программы обучения", 'link' : 'lancen:courses_list'},
    {'title' : "Контакты", 'link' : 'lancen:contact'},
]


admin_pers_area_items = [
    {'title' : "Листы посещаемости и успеваемости", 'link': 'journal:journals'},
]
if LearingGroup.objects.annotate(Count('name')):
    admin_pers_area_items.append({'title' : "Автоматическое создание расписания" , 'link' : 'timetable:create_timetable'})

    
teacher_pers_area_items = [
    #{'title': "Мои ученики", 'link': "profiles:student_list" },
    {'title': "Журналы успеваемости", 'link': 'journal:journals'},
    # {'title': "Домашние задания", "link": 'homework:homework_list'},
]

student_pers_area_items = [
    {'title' : 'Мои баллы', "link": "journal:student_marks"},
    {'title' : "Список приобретённых абонементов", "link": 'abonements:student_abonements'},
    {'title' : "Список доступных занятий", "link" : 'abonements:student_payment_lessons'},
]




class DataMixin():

    def get_user_context(self, **kwargs):
        context = kwargs


        modern_menu = menu.copy()

      

        if  self.request.user.is_authenticated:
            modern_menu.append({'title' : "Личный кабинет" , 'link' : 'profiles:personal_area'})


        if self.request.user.groups.filter(name='teacher').exists():
            context["pers_area_items"] = teacher_pers_area_items
        
        if self.request.user.groups.filter(name='student').exists():
            context["pers_area_items"] = student_pers_area_items


        if self.request.user.is_superuser:
            modern_menu.append({'title' : "Перейти в админ панель" , 'link' : 'profiles:admin'})
            context["pers_area_items"] = admin_pers_area_items

            

        context['menu'] = modern_menu

        context["recall_form"] = RecallForm
        context['contact_form'] = ContactForm
        

        return context




def teacher_or_admin_valid(request):
    if not (request.user.groups.filter(name='teacher').exists() or request.user.is_superuser):
        print("Зашёл пользователь не с теми правами доступа")
        raise PermissionDenied()

def get_student(id):
    try:
        return Student.objects.get(pk = id)
    except:
        return False

def get_teacher(id):
    try:
        return Teacher.objects.get(pk = id)
    except:
        return False