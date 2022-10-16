from django import template

from app_homework.models import *


register = template.Library()

@register.simple_tag()
def get_files(id_hw):
    try:
        # hw = Homework.objects.get()
        files = FileHomework.objects.filter(homework = id_hw)
        return files
    except:
        return []