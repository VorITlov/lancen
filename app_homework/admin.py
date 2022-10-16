from django.contrib import admin
from .models import *
# Register your models here.





class FileHomeworkInLine(admin.StackedInline):
    model = FileHomework

class HomeworkAdmin(admin.ModelAdmin):
    inlines = [FileHomeworkInLine]

admin.site.register(Homework, HomeworkAdmin)

