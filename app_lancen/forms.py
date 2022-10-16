from django import forms
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError




phone_params = {
    'class': 'phone mb-3', 
    "onkeypress": "validate_phone(event);",  
    "placeholder" : "89999999999",
}


class FreeLesson(forms.Form):
    name = forms.CharField(label =  "Ваше имя",  max_length=255, widget=forms.TextInput({'placeholder' : ""}))
    email = forms.EmailField(label="Ваша почта", widget=forms.EmailInput({'placeholder' : "mail@email.com"}))
    phone = forms.CharField(label = "Номер телефона", max_length= 11, min_length=11, widget=forms.TextInput(attrs=phone_params))
    captcha = CaptchaField(label = "")
    sogl = forms.BooleanField(label="Согласие на обработку персональных данных")

    


class RecallForm(forms.Form):
    phone = forms.CharField(label="Номер телефона", max_length=11, min_length=11, widget=forms.TextInput(attrs=phone_params))
    captcha = CaptchaField(label = "", )
    sogl = forms.BooleanField(label="Согласие на обработку персональных данных")



class ContactForm(forms.Form):
    name = forms.CharField(label =  "Ваше имя", max_length=255, widget=forms.TextInput({'placeholder' : ""}))
    email = forms.EmailField(label="Ваша почта",  widget=forms.EmailInput({'placeholder' : "mail@email.com"}))
    text = forms.CharField(widget=forms.Textarea, label="Ваш вопрос")
    captcha = CaptchaField(label = "", )
    
