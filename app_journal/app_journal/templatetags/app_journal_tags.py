
from django import template

from app_journal.models import Attendance, Mark
from app_profiles.models import Student
from app_timetable.models import TimeTable


register = template.Library()


@register.simple_tag()
def test():
    return "It Works!"



@register.simple_tag()
def is_was(id_student , id_lesson):
   
    stud = Student.objects.get(id = id_student)
    attendance = Attendance.objects.filter(student=stud, lesson_date = id_lesson, was = True)
    if attendance:
        return True
    else:
        return False

@register.simple_tag()
def get_marks(id_student, id_lesson):
    stud = Student.objects.get(id = id_student)
    lesson = TimeTable.objects.get(id = id_lesson)
    marks = Mark.objects.filter(student = stud, lesson_date = lesson)
    return marks



@register.simple_tag()
def mark_sum(*args, **kwargs):
    sum = 0
    for item in args:
        sum += item
    return sum