
from django import template


from app_timetable.models import TimeTable


register = template.Library()



@register.simple_tag()
def get_last_lesson_abonement(obj):
    """Получает последнее занятие в текщем абонементе"""
    last_date = TimeTable.objects.filter(group = obj.student.group, date__gte = obj.date_start)[obj.abonement.amount_lesson -2]
    # print(type(last_date.date))
    return last_date.date or False



@register.simple_tag()
def get_result_price_value(a,b):
    """Получает цену с учётом скидки"""
    return int(a) - int(b)