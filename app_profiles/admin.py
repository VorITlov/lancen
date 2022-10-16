from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from app_profiles.models import *

# Register your models here.





class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    


    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["password"].label = "Дибильный пароль"
        form.base_fields["first_name"].required = True
        form.base_fields["last_name"].required = True

        return form

    def save_model(self, request, obj, form, change):
        if obj.pk:
            orig_obj = Teacher.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()


class StudentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
       

        if obj.pk:
            orig_obj = Student.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)

