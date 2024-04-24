from django import template

from app_lancen.utils import get_student, get_teacher

from app_profiles.models import *
from app_abonements.models import PaymentAbonement
# from django.template.loader import get_template
register = template.Library()




def get_template_according_role(request):
    """Возвращает шаблон в соответсвии с ролью"""
    pass






@register.simple_tag() 
def teacher_or_student(user_id):
    if get_student(user_id):
        return "student"
    elif get_teacher(user_id):
        return "teacher"
    else:
        return False




@register.inclusion_tag('templatetags/app_profiles/teacher_profile.html')
def teacher_profile(id_user):
    teacher = Teacher.objects.get(pk = id_user)
    return {'teacher': teacher }

@register.inclusion_tag('templatetags/app_profiles/student_profile.html')
def student_profile(id_user):
    student = Student.objects.get(pk = id_user)
    abonement_info =  PaymentAbonement.objects.filter(student_id = id_user).order_by('-id')[0]
    return {'student': student, 'abonement_info': abonement_info}