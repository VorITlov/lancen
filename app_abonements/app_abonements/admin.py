from django.contrib import admin


from .models import *
from .forms import * 
# Register your models here.




class StudentPaymenatLessonsAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'payment_abonement')
    list_filter = ('lesson__group', 'payment_abonement__student__last_name')




class PaymentAbonementAdmin(admin.ModelAdmin):
    form = PaymentAbonementForm

    list_display = ('student', 'abonement', 'date_start', 'date_payment', 'discount')
    list_filter = ('student__group', 'student__last_name')

    # @admin.display(empty_value='???', description="Цена абонемента")
    # def view_price_abonement(self, obj):
    #     return obj.abonement.price

    def save_model(self, request, obj, form, change):
       
        lessons = search_lesson(
            form.cleaned_data["student"], 
            form.cleaned_data["date_start"],
            form.cleaned_data["abonement"]
        )
        model =  form.save()
        create_lesson(lessons_list=lessons, abonement=model)

       
    
admin.site.register(Abonement)
admin.site.register(PaymentAbonement, PaymentAbonementAdmin)
admin.site.register(StudentPaymenatLessons, StudentPaymenatLessonsAdmin)