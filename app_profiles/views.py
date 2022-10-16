from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls.base import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic import ListView
from app_lancen.utils import *
from .models import Student, Teacher 
from app_journal.models import Journal
from .forms import *

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.



class LoginUser(DataMixin,LoginView):
    form_class = AuthenticationForm
    template_name = 'app_profiles/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_context = self.get_user_context(title = "Авторизация")
        return dict(list(context.items()) + list(data_mixin_context.items()))

    def get_success_url(self):
        return reverse_lazy('profiles:personal_area')


class Logout(LogoutView):
    next_page = reverse_lazy('profiles:login')



class PersonalArea(DataMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('profiles:login')
    template_name = 'app_profiles/personal-area.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_context = self.get_user_context(title = "Личный кабинет", test = "test")

        if self.request.user.groups.filter(name='teacher').exists():
            context["techer_user"] = Teacher.objects.get(id = self.request.user.id)
        
        if self.request.user.groups.filter(name='student').exists():
            context["student_user"] = Student.objects.get(id = self.request.user.id)


        return dict(list(context.items()) + list(data_mixin_context.items()))


class ShowStudentForTeacher(DataMixin,LoginRequiredMixin, ListView):
    model = Student
    paginate_by = 10
    template_name = "app_profiles/teachers_student.html"

    def get_queryset(self):
        try:
            search_param = self.request.GET.get("search")
            query = Student.objects.filter(
                    group__in = [jl.group.id for jl in Journal.objects.filter(teacher = self.request.user)],
                )

            if search_param:
                print("sep")
                return query.filter(
                    Q(first_name__contains = search_param ) | Q(last_name__contains = search_param)
                    )
            return query
        except:
            return []
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_form"] = SearchStudentForm(self.request.GET ,search_param = self.request.GET.get("search"))

        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': '#',  'title' : "Список студентов"}
        ]

        data_mixin_context = self.get_user_context(title = "Список студентов")
        return dict(list(context.items()) + list(data_mixin_context.items()))


class EditStudentProfile(DataMixin,TeacherPermission, UpdateView):
    """Редактирование профиля учителя"""

    model = Student
    form_class = EditStudentForm
    success_url = reverse_lazy('profiles:personal_area')
    template_name = "app_profiles/edit_student_profile.html"

    def get_object(self):
        return Student.objects.get(pk = self.kwargs["id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["photo"] = self.model.photo
        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': '#',  'title' : "Редактирование профиля"}
        ]

        data_mixin_context = self.get_user_context(title = "Редактирование профиля")
        return dict(list(context.items()) + list(data_mixin_context.items()))


class ChangePassword(DataMixin, LoginRequiredMixin, FormView):
    """Смена пароля"""
    
    success_url = reverse_lazy('profiles:personal_area')
    
    def get_form(self) :
        form = PasswordChangeForm(user=self.request.user, data=self.request.POST)
        return  form

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': '#',  'title' : "Смена пароля"}
        ]

        data_mixin_context = self.get_user_context(title = "Смена пароля")
        return dict(list(context.items()) + list(data_mixin_context.items()))

    
    
