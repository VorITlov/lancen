from django import forms
import datetime

from app_lancen.models import *
from .models import TimeTable

class DateInputWidget(forms.DateInput):
    input_type = 'date'

    def format_value(self, value):
        return value


class CreateTimetableForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        groups = LearingGroup.objects.all()
        """Выбор группы"""
        choices =[(item.id, item.name) for item in groups]
        self.fields["group"] = forms.ChoiceField(choices=choices , label="Группа")
        

    
    
   
    """Выбор дней недели"""
    choices_day = [
        ('0', 'понедельник'),
        ('1', 'вторник'),
        ('2', 'среда'),
        ('3', 'четверг'),
        # ('4', 'пятница'),
        # ('5', 'суббота'),
        # ('6', 'воскресение'),

    ]
    day = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required= True,
        choices=choices_day,
        label='День(дни) недели'
    )


    """Выбор даты старта"""
    day_start = forms.DateField(
        widget=DateInputWidget(),
        label='Дата старта расписания'
    )

    choices_diap_day = [
        ('7', 'на неделю'),
        ('31', 'на месяц'),
        ('183', 'на полгода'),
        ('365', 'на год'),
    ]
    diap = forms.ChoiceField(choices=choices_diap_day , label="на какой период создаётся расписание")


    # def test_get_data(self, *args):
    #     print(f"{args}")

    def create_timetable(self, start_date, amount_itteration , day_index, group):
        # print(f"{start_date} , {amount_itteration}, {day_index}")
        count = 0
        iter_day = start_date
        group_model = LearingGroup.objects.get(pk = group)
        while count < int(amount_itteration):

            iter_day = iter_day + datetime.timedelta(days=1)
            day_week_iter_day = datetime.datetime(day = iter_day.day, month = iter_day.month, year = iter_day.year).weekday()

            #print(iter_day)

            for item in  day_index:
                if int(item) == int(day_week_iter_day):
                    # print(f"{item} ==> {day_week_iter_day} ==> {iter_day}")
                    gs = TimeTable(group = group_model, date = iter_day)
                    gs.save()            
            #print(f"{datetime.datetime(day = iter_day.day, month = iter_day.month, year = iter_day.year).weekday()}")

            count += 1

