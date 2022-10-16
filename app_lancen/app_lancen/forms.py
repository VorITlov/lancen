from django import forms
from captcha.fields import CaptchaField




class FreeLesson(forms.Form):
    name = forms.CharField(label =  "Ваше имя", max_length=255)
    email = forms.EmailField(label="Ваша почта")
    phone = forms.CharField(label = "Номер телефона", max_length= 10, widget=forms.TextInput(attrs={'class': 'phone mb-3', "id": "phone"}))
    captcha = CaptchaField(label = "")


class RecallForm(forms.Form):
    phone = forms.CharField(label="Номер телефона")
    captcha = CaptchaField(label = "", )


class ContactForm(forms.Form):
    name = forms.CharField(label =  "Ваше имя", max_length=255)
    email = forms.EmailField(label="Ваша почта")
    text = forms.CharField(widget=forms.Textarea, label="Ваш вопрос")