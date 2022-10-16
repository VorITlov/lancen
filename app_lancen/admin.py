from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(LearingGroup)
admin.site.register(TrainingProgramm)

admin.site.site_title = "Админ панель"
admin.site.site_header = "Настройки языкового центра"