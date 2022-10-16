from django import forms

from app_homework.models import Homework
from app_journal.models import Journal

class CreateHomeworkForm(forms.ModelForm):

    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, label='Файлы')
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['date'] = forms.DateField(label="Дата выдачи", widget=forms.DateInput(format='%Y-%m-%d', attrs={"type":"date"} ))
        if user: 
            self.fields['journal_list'].queryset = Journal.objects.filter(teacher = user)
            self.fields['journal_list'].empty_label = None
            self.fields['journal_list'].help_text = """ 
            Если в выпадающем спсике нет элементов, 
            значит вам следует обратиться к администратору. 
            Журнальные листы не добавлены. Создание дз невозможно
            """
    class Meta:
        model = Homework
        fields = ('name', 'date', 'description', 'journal_list',)



class OrderHomeworkGroup(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        group_choises = [(item.group.id, item.group.name) for  item in Journal.objects.filter(teacher = user) ]
        group_choises.insert(0,('', 'Все группы'))

        self.fields['group'] = forms.ChoiceField(label="Выбор группы", choices=group_choises, required=False, widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['group'].empty_label = "---"