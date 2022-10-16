from django import forms
from .models import *

class EditStudentForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['password'] = forms.CharField(label="Пароль", help_text="Если хотите изменить пароль, просто очистите поле, и введите новый пароль", widget=forms.TextInput(attrs={"type": "password"}))
       
    
    #password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = ("username", "email", "photo")

        

class SearchStudentForm(forms.Form):

    def __init__(self, *args, **kwargs):
        kwargs.pop('search_param', None)
        super().__init__(*args, **kwargs)
        

    search = forms.CharField(
        label="Поиск студента", 
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={'class': "form-control"}))
