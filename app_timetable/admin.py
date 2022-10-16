from django.contrib import admin
from .models import *

# Register your models here.



class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('group', 'date', 'comment')
    list_filter = ('group',)

admin.site.register(TimeTable, TimeTableAdmin)