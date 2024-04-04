from django.shortcuts import render
from .models import *
from .forms import *
from app_lancen.utils import *

from django.urls.base import reverse


# Create your views here.

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class AbonementDeatil(DataMixin, DetailView):
    """Отображает информацию об абонементе"""

    model = Abonement
    template_name = "app_abonements/abonement_detail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        abonement = Abonement.objects.get(id = self.kwargs["pk"])
        course = TrainingProgramm.objects.get(id = self.kwargs["id_course"])

        context['breadcrumbs'] = [
            {'link': reverse('lancen:index'), 'title':'Главная'},
            {'link': reverse('lancen:courses_list'), 'title':'Программы обучения'},
            {'link': reverse('lancen:course_view', args=[course.id]),'title': course.name},
            {'link' : '#', 'title': str(abonement.name)}
        ]

        data_mixin_context = self.get_user_context(title = abonement.name)
        return dict(list(context.items()) + list(data_mixin_context.items()))


class StudentAbonementsView(DataMixin, LoginRequiredMixin, ListView):
    """Показывает студенту список его абонементов"""

    template_name = "app_abonements/student_abonements.html"
    paginate_by =  10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': '#', 'title': "Мои приобретёные абонементы"}
        ]

        data_mixin_context = self.get_user_context(title = "Оплаченные абонементы")
        return dict(list(context.items()) + list(data_mixin_context.items()))

    def get_queryset(self):
        return  PaymentAbonement.objects.filter(student = self.request.user).order_by('-date_start')

    

class StudentPaymentLesson(DataMixin, LoginRequiredMixin, ListView):
    """Показывает студенту, на какие занятия он может ходить"""
    paginate_by = 20
    template_name = "app_abonements/student_payment_lessons.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sort_form'] = SortStudentAbonement(self.request.GET, stud = self.request.user)


        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link' : reverse('abonements:student_abonements'), 'title' : 'Оплаченные абонементы'},
            {'link': '#', 'title': "Занятия доступные мне"}
        ]

        data_mixin_context = self.get_user_context(title = "Доступные занятия")
        return dict(list(context.items()) + list(data_mixin_context.items()))

    def get_queryset(self):
       return StudentPaymenatLessons.objects.filter(payment_abonement__student = self.request.user, payment_abonement_id = self.kwargs["id_payment_abonement"]).order_by('-lesson__date')
