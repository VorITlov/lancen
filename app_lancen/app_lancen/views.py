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

    # def post(self, request, *args, **kwargs):
    #     context = self.get_context_data()
    #     return super(TemplateView, self).render_to_response(context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = FreeLesson
        data_mixin_context = self.get_user_context(title = "Главная страница")
        return dict(list(context.items()) + list(data_mixin_context.items()))




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
            data_dict = {
                "name": name,
                "status": 0,
                'new_cptch_key' : key,
                'new_cptch_image' :  captcha_image_url(key),
            }

            print(f"Вот тут я пытаюсь отпрвить письмо на почту\n {name} челу")


            """
            send_mail(
                f"Заявка на бесплатное занятие",
                f'Имя и номер телефона: {form.cleaned_data["name"]} => {form.cleaned_data["phone"]}',
                'vorotilov.01@mail.ru',
                ['grigoranov@gmail.com'],
            )
            """ 

            mail = 1 #сюда вставится закомментируемая функция
            
            time.sleep(2)

            if mail>0:
                data_dict["success"] = "Письмо успешно отправлено на указанную почту"
            else:
                data_dict["error"] = "Ошибка отправки письма"



            print(f"Конец попытки отправки почты")


            return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})
       

    def form_invalid(self, form):
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            print("Ну я хотя бы попытался")
            key = CaptchaStore.generate_key()
            data_dict = {
                "post_values" : json.loads(self.request.body.decode("utf-8")),
                "forms_values" : form.cleaned_data,
                "errors": form.errors,
                "status": 1,
                'new_cptch_key' : key,
                'new_cptch_image' :  captcha_image_url(key),

            }
            return JsonResponse(data_dict,json_dumps_params={'ensure_ascii': True})
       

   

class ContactView(DataMixin,TemplateView):
    """Отображение страницы Контакты"""

    template_name = 'app_lancen/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_context = self.get_user_context(title = "Контакты")
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

        data_mixin_context = self.get_user_context(title = "Программа обучения")
        return dict(list(context.items()) + list(data_mixin_context.items()))