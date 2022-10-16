from django.shortcuts import render
from django.http.response import  HttpResponseRedirect
from app_homework.models import FileHomework, Homework
from app_lancen.utils import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.views.generic.dates import WeekArchiveView
from django.views.generic import ListView
from django.urls.base import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin





class HomeworkList(DataMixin,LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Список из дз для учителя"""
    model = Homework
    paginate_by = 20
    template_name = "app_homework/homework_list_teacher.html"

    def has_permission(self):
        return get_teacher(self.request.user.id)

    def get_queryset(self):

        group_param = self.request.GET.get('group')

        if group_param:
            query = Homework.objects.filter(journal_list__teacher = self.request.user, journal_list__group  = group_param ).order_by('-date')
        else:
            query = Homework.objects.filter(journal_list__teacher = self.request.user).order_by('-date')


        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': '#',  'title' : "Домашние задания"}
        ]

        context["order_by_group_form"]  = OrderHomeworkGroup(self.request.GET, user = self.request.user)


        data_mixin_context = self.get_user_context(title = "Домашние задания")
        return dict(list(context.items()) + list(data_mixin_context.items()))






class HomeworkListStudent(DataMixin,LoginRequiredMixin,  WeekArchiveView):
    queryset = Homework.objects.all()
    template_name = "app_homework/homework_for_student.html"
    date_field = "date"
    week_format = "%W"
    allow_future = True
    allow_empty = True

    

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': '#',  'title' : "Домашние задания"}
        ]

        data_mixin_context = self.get_user_context(title = "Домашние задания")

        return dict(list(context.items()) + list(data_mixin_context.items()))



class UpdateHomework(DataMixin,LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Homework
    template_name = "app_homework/update_homework.html"
    form_class = CreateHomeworkForm
    success_url = reverse_lazy('homework:homework_list')

    def has_permission(self):
        return get_teacher(self.request.user.id)
        
    def get_object(self):
        return Homework.objects.get(pk = self.kwargs["id"])


    def form_valid(self, form):
        files = self.request.FILES.getlist('files')
        id = form.save().pk
        hw = Homework.objects.get(pk = id)
        if files:
            for f in files:
                fl = FileHomework(file = f, homework = hw)
                fl.save()
            print("Прошло сохранение формы")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': reverse('homework:homework_list'), 'title':'Домашние задания'},
            {'link': '#',  'title' : "Редактирвание дз"}
        ]

        context["files"] = FileHomework.objects.filter(homework = self.kwargs["id"])
        context['id_hw'] = self.kwargs["id"]

        data_mixin_context = self.get_user_context(title = "Редактирвоание дз")
        return dict(list(context.items()) + list(data_mixin_context.items()))

def delete_file(request,id_file, id_hw):
    try:
        file = FileHomework.objects.get(pk = id_file)
        file.delete()
    except:
        print(f"Ошибка удаления")
    finally:
        return HttpResponseRedirect(reverse_lazy('homework:update_homework', args=[id_hw]))


class DeleteHomework(TeacherPermission, DeleteView):
    model = Homework
    success_url = reverse_lazy('homework:homework_list')
    template_name = "app_homework/delete_homework.html"

    def has_permission(self):
        return super().has_permission()

    def get_object(self):
        return Homework.objects.get(pk = self.kwargs["id"])

    


class ExposeHomework(DataMixin, TeacherPermission, CreateView):

    login_url = reverse_lazy('profiles:login')
    model = Homework
    form_class = CreateHomeworkForm
    template_name = "app_homework/expose_homework.html"

    def has_permission(self):
        return super().has_permission()

    def get_success_url(self):
        return reverse_lazy('homework:homework_list')

    def get_form_kwargs(self):
        kwargs = {'initial': self.get_initial()}
        kwargs.update({'user': self.request.user})

        if self.request.method in ('POST', 'PUT'):

            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })

        return kwargs

    def form_valid(self, form):
        files = self.request.FILES.getlist('files')
        id = form.save().pk
        hw = Homework.objects.get(pk = id)
        if files:
            for f in files:
                fl = FileHomework(file = f, homework = hw)
                fl.save()
                
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': reverse('homework:homework_list'), 'title':'Домашние задания'},
            {'link': '#',  'title' : "Выдача дз"}
        ]

        data_mixin_context = self.get_user_context(title = "Выдача дз")
        return dict(list(context.items()) + list(data_mixin_context.items()))

    
