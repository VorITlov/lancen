from django.http import JsonResponse
from django.views.generic import ListView, DetailView, FormView

from django.views.generic.base import TemplateView
from app_abonements.models import Abonement
from .forms import *

from app_lancen.models import TrainingProgramm

from django.urls.base import reverse

from django.core.mail import send_mail
import time


# Create your views here.

from .utils import *

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json


class IndexPageView(DataMixin,TemplateView):
    """Рендер главной страницы"""
    template_name = 'app_lancen/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = FreeLesson
        data_mixin_context = self.get_user_context(title = "Языковой центр UNILINGVO")
        return dict(list(context.items()) + list(data_mixin_context.items()))
   

class ContactView(DataMixin,TemplateView):
    """Отображение страницы Контакты"""

    template_name = 'app_lancen/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_context = self.get_user_context(title = "Контакты языкового центра Unilingvo")
        return dict(list(context.items()) + list(data_mixin_context.items()))


class StockView(DataMixin,TemplateView):
    """Отображение страницы Акции"""

    template_name = 'app_lancen/stock.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_context = self.get_user_context(title = "Акции языкового центра")
        return dict(list(context.items()) + list(data_mixin_context.items()))




class TrainingProgrammList(DataMixin, ListView):
    """Отображение страницы программы обучения"""
    template_name = "app_lancen/course_list.html"
    def get_queryset(self):
        return TrainingProgramm.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_context = self.get_user_context(title = "Программы обучения")
        return dict(list(context.items()) + list(data_mixin_context.items()))

class TrainingProgrammDetail(DataMixin, DetailView):
    model = TrainingProgramm
    template_name = "app_lancen/course_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        course = TrainingProgramm.objects.get(id = self.kwargs["pk"])

        context['breadcrumbs'] = [
            {'link': reverse('lancen:index'), 'title':'Главная'},
            {'link': reverse('lancen:courses_list'), 'title':'Программы обучения'},
            {'link': '#', 'title': course.name}
        ]

        context["abonements"] = Abonement.objects.filter(course = course)

        data_mixin_context = self.get_user_context(title = f"Абонементы для {course.name}" )
        return dict(list(context.items()) + list(data_mixin_context.items()))


class SendMailFormView(FormView):
    """Обработка формы 'Задайте нам вопрос' """
    
    template_name = 'app_lancen/forms/send_mail.html'

    def get_form(self):
        data = json.loads(self.request.body.decode("utf-8"))
        return ContactForm(data)
    
    def form_valid(self, form):
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            key =  CaptchaStore.generate_key()
            data_dict = {"status": 0,'new_cptch_key' : key,'new_cptch_image' :  captcha_image_url(key)}

            mail = send_mail(
                f"Вопрос от {form.cleaned_data['email']} => {form.cleaned_data['name']} ",
                f'Вопрос: {form.cleaned_data["text"]}',
                'vorotilov.01@mail.ru',
                ['grigoranov@gmail.com'],
            ) 
            

            if mail>0:
                data_dict["success"] = "Письмо успешно отправлено на указанную почту"
            else:
                data_dict["error"] = "Ошибка отправки письма"

            return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})
       

    def form_invalid(self, form):
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            key = CaptchaStore.generate_key()
            data_dict = {"errors": form.errors,"status": 1,'new_cptch_key' : key,'new_cptch_image' :  captcha_image_url(key)}
            return JsonResponse(data_dict,json_dumps_params={'ensure_ascii': True})


class RecallFormView(FormView):
    """Обработка формы 'Мы вам перезвоним' """

    template_name = 'app_lancen/forms/recall.html'

    def get_form(self):
        data = json.loads(self.request.body.decode("utf-8"))
        return RecallForm(data)

    def form_valid(self, form):
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            key =  CaptchaStore.generate_key()
            data_dict = {"status": 0,'new_cptch_key' : key,'new_cptch_image' :  captcha_image_url(key)}

            mail =  send_mail(
                f"Заявка на ответный звонок",
                f'Перезвонить на номер телефона: {form.cleaned_data["phone"]}',
                'vorotilov.01@mail.ru',
                ['grigoranov@gmail.com'],
            )
            
         
            if mail>0:
                data_dict["success"] = "Письмо успешно отправлено на указанную почту"
            else:
                data_dict["error"] = "Ошибка отправки письма"

            return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})
       

    def form_invalid(self, form):
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            key = CaptchaStore.generate_key()
            data_dict = {"errors": form.errors,"status": 1,'new_cptch_key' : key,'new_cptch_image' :  captcha_image_url(key)}
            return JsonResponse(data_dict,json_dumps_params={'ensure_ascii': True})


class FreeLessonFormView(FormView):
    """Обработка формы заявки на бесплатное занятие"""

    template_name = 'app_lancen/forms/free_lesson.html'
    
    def get_form(self):
        data = json.loads(self.request.body.decode("utf-8"))
        return FreeLesson(data)
    
    def form_valid(self, form):
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            name = form.cleaned_data['name']
            key =  CaptchaStore.generate_key()
            data_dict = {"name": name,"status": 0,'new_cptch_key' : key,'new_cptch_image' :  captcha_image_url(key),}

            mail =  send_mail(
                f"Заявка на бесплатное занятие от {form.cleaned_data['email']}",
                f'Имя и номер телефона: {form.cleaned_data["name"]} => {form.cleaned_data["phone"]}',
                'vorotilov.01@mail.ru',
                ['grigoranov@gmail.com'],
            )
           
            if mail>0:
                data_dict["success"] = "Письмо успешно отправлено на указанную почту"
            else:
                data_dict["error"] = "Ошибка отправки письма"

            return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})
       

    def form_invalid(self, form):
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            key = CaptchaStore.generate_key()
            data_dict = {"post_values" : json.loads(self.request.body.decode("utf-8")),"forms_values" : form.cleaned_data,"errors": form.errors,"status": 1,'new_cptch_key' : key,'new_cptch_image' :  captcha_image_url(key)}
            return JsonResponse(data_dict,json_dumps_params={'ensure_ascii': True})
       
