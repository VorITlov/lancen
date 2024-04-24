from django import template

from app_homework.models import *
from re import findall


register = template.Library()

@register.simple_tag()
def get_files(id_hw):
    try:
        # hw = Homework.objects.get()
        files = FileHomework.objects.filter(homework = id_hw)
        return files
    except:
        return []
    


@register.simple_tag()
def get_links_in_text(text: str):
    text_list = text.split()
    for i in range(len(text_list)):
        print(text_list[i])
        index = text_list[i].find('http')
        print(index)
        if  index != -1:
            print("NOT")
            text_list[i] = link_converter(text_list[i])
    print(text_list)
    return ' '.join(str(el) for el in text_list)

    
def link_converter(link:str):
    return f'<a href = "{link}">{link}</a>'

