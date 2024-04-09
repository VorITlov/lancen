from django.contrib import admin
from .models import *

# Register your models here.



class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('group', 'date','canceled', 'comment')
    list_filter = ('group', 'canceled')
    search_fields= ('date',)

admin.site.register(TimeTable, TimeTableAdmin)