from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from app_lancen.utils import DataMixin
from .forms import *
from django.urls.base import reverse, reverse_lazy
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateTimetablesFormView(DataMixin,LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'app_timetable/create_timetable.html'
    #form_class = CreateTimetableForm
    success_url = reverse_lazy('timetable:create_timetable')
    success_message = "Расписание создано успешно. Список созданных занятий доступен в административной панели"

    def get_form(self, form_class = None):
        if self.request.POST:
            form = CreateTimetableForm(self.request.POST)
        else:
            form =  CreateTimetableForm()
        form.order_fields(field_order=['group', 'day', 'day_start', 'diap'])
        return form

    def form_valid(self, form):
        form.create_timetable(
            start_date = form.cleaned_data['day_start'],
            amount_itteration = form.cleaned_data['diap'],
            day_index = form.cleaned_data['day'],
            group = form.cleaned_data['group']
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_context = self.get_user_context(title = "Автоматическое создание расписания")

        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': '#', 'title': "Автоматическое создание расписания"}
        ]

        return dict(list(context.items()) + list(data_mixin_context.items()))
