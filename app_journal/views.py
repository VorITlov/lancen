from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.views.generic.dates import MonthArchiveView
from app_journal.models import *
from app_lancen.utils import *
from .forms import *



from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from django.urls.base import reverse
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

# Create your views here.


class TeachersJournalList(DataMixin, LoginRequiredMixin, ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_context = self.get_user_context(title = "Листы посещаемости и успеваемости")


        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': '#', 'title': "Журнальные листы"}
        ]


        return dict(list(context.items()) + list(data_mixin_context.items()))

    def get_queryset(self):
        if self.request.user.is_superuser:
            journals = Journal.objects.all()
        
        if self.request.user.groups.filter(name='teacher').exists():
            teacher = Teacher.objects.get(id = self.request.user.id)
            journals = Journal.objects.filter(teacher = teacher)

        return journals



class JournalMonthView(DataMixin,TeacherPermission, MonthArchiveView):
    """Отображение журнального листа с оценками и посещаемостью для учителя и администратора"""
    template_name = 'app_journal/view-journal.html'
    date_field = "date"
    allow_future = True
    allow_empty = True

    def has_permission(self):
        return super().has_permission()


    def get_queryset(self):
        return TimeTable.objects.filter(group=self.kwargs['group']).order_by('date')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        group_student = LearingGroup.objects.get(id = self.kwargs['group'] )
        context["group_list"] = Student.objects.filter(group = self.kwargs['group'])
        context["info_group"] = group_student
        context['date_for_m_y'] = date(year=self.kwargs["year"], month=self.kwargs["month"], day=1)

        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': reverse('journal:journals'), 'title': "Журнальные листы"},
            {'link': '#',  'title' : f"Журнальный лист {group_student.name}"}
        ]

        data_mixin_context = self.get_user_context(title = "Просмотр журнального листа")
        return dict(list(context.items()) + list(data_mixin_context.items()))



class ExposeMark(TeacherPermission, FormView):
    model = Mark
    form_class = ExposeMarkForm
    template_name = 'app_journal/expose_mark.html'

    def has_permission(self):
        return super().has_permission()

    def get_success_url(self): 
        date_list = self.kwargs['date'].split("-")
        group = Student.objects.get(id = self.kwargs["student"]).group.id
        return reverse('journal:view-journal', args=[group,date_list[0], date_list[1]])

    def form_valid(self, form):
        mark = form.save(commit = False)
        stud = Student.objects.get(id = self.kwargs["student"])
        lesson = TimeTable.objects.get(id =self.kwargs["lesson_date"] )
        mark.student = stud
        mark.lesson_date = lesson
        mark.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #<int:student>/<int:lesson_date>/<str:date>
        context["student"] = self.kwargs["student"]
        context["lesson_date"] = self.kwargs["lesson_date"]
        context["date"] = self.kwargs["date"]

        return context



class UpdateMark(TeacherPermission, UpdateView):
    model = Mark
    form_class = ExposeMarkForm
    template_name = 'app_journal/update_mark.html'

    def has_permission(self):
        return super().has_permission()

    def get_success_url(self):
        return reverse('journal:view-journal', args=[self.kwargs['id_group'],self.kwargs['year'], self.kwargs['month']])

    def get_object(self):
        return get_object_or_404(Mark, pk=self.kwargs['id_mark'])

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #<int:id_mark>/<int:id_group>/<int:year>/<str:month>/
        context["id_mark"] = self.kwargs["id_mark"]
        context["id_group"] = self.kwargs["id_group"]
        context["year"] = self.kwargs["year"]
        context["month"] = self.kwargs["month"]
        print(f"{context}")
        return context
    

def delete_mark(request, id_mark):
    response_data = {}
    teacher_or_admin_valid(request=request)
    try:
        mark = Mark.objects.get(id = id_mark)
        mark.delete()
        response_data["result"] = "Оценка удалена"
    except:
        response_data["result"] = "Ошибка удаления"

    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})




def expose_attendance(request, stud_id, timetable_id):
    """Выставление аспекта посещаемости"""
    response_data = {}
    teacher_or_admin_valid(request=request)
    try:
        stud = Student.objects.get(id = stud_id)
        timetable = TimeTable.objects.get(id=timetable_id)

        item = Attendance(student = stud, lesson_date = timetable, was = True)
        item.save()
        response_data['result'] = 'Посещаемость выставлена студенту'
        print("Выставление прошло успешно")
    except:
        response_data['result'] = 'Ошибка выставления аспекта посещаемости'
        print("Ошибка выставления")

    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})



def delete_attendance(request,stud_id, timetable_id):
    """удаление аспекта посещаемости аспекта посещаемости"""
    response_data = {}
    teacher_or_admin_valid(request=request)
    try:
        stud = Student.objects.get(id = stud_id)
        item = Attendance.objects.filter(student = stud, lesson_date = timetable_id)
        item.delete()
        response_data['result'] = 'Аспект посещаемости удалился'
    except:
        response_data['result'] = 'Ошибка удаления аспекта посещаемости'
        print("Ошибка удаления")

    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})


@method_decorator(login_required, name="dispatch")
class StudentMarkView(DataMixin, ListView):
    template_name = "app_journal/student_marks.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_context = self.get_user_context(title = "Мои баллы")

        context['breadcrumbs'] = [
            {'link': reverse('profiles:personal_area'), 'title':'Личный кабинет'},
            {'link': '#', 'title': "Мои баллы"}
        ]


        return dict(list(context.items()) + list(data_mixin_context.items()))

    def get_queryset(self):
        stud = Student.objects.get(id = self.request.user.id)
        marks = Mark.objects.filter(student = stud).order_by('-lesson_date__date')
        return marks




