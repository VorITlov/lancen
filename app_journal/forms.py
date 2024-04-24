from django import forms

from app_journal.models import Mark

class ExposeMarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['work_on_lesson', 'behavior', 'extra', 'homework','additional']

   