from django.contrib import admin


from .models import *
from .forms import * 
# Register your models here.




class StudentPaymenatLessonsAdmin(admin.ModelAdmin):
    """Оплаченные занятия пользователей"""

    list_display = ('stduent_surname_name','abonement_name', 'lesson_date')
    #list_filter = ('lesson__group', 'payment_abonement__student__last_name')
    list_filter = ('payment_abonement__student__last_name', 'payment_abonement__student__group')

    @admin.display(description="Дата занятия", empty_value='???')
    def lesson_date(self, obj):
        return f"{obj.lesson.date} в {obj.lesson.group} группе"

    @admin.display(description="Студент", empty_value='???')
    def stduent_surname_name(self, obj):
        surname_name = obj.payment_abonement.student.last_name + ' ' + obj.payment_abonement.student.first_name
        return surname_name

    @admin.display(description="Абонемент", empty_value='???')
    def abonement_name(self, obj):
        return f"{obj.payment_abonement.abonement.name} {obj.payment_abonement.abonement.amount_lesson} занятий Oплата:({obj.payment_abonement.date_payment})"





class PaymentAbonementAdmin(admin.ModelAdmin):
    """Оплаты абонементов"""

    form = PaymentAbonementForm

    list_display = ('student', 'abonement',  'date_need_new_abonement', 'date_start', 'date_payment', 'result_price')
    list_filter = ('student__group', 'student__last_name')
    ordering = ('student__group', )

    # @admin.display(empty_value='???', description="Последнее занятие")
    # def last_lesson(self, obj):
    #     last_date = TimeTable.objects.filter(group = obj.student.group, date__gte = obj.date_start)[obj.abonement.amount_lesson -1]
    #     return last_date.date or False

    
    @admin.display(empty_value='???', description="Рекоменд. дата след. оплаты")
    def date_need_new_abonement(self, obj):
        date_need_pay = TimeTable.objects.filter(group = obj.student.group, date__gte = obj.date_start)[obj.abonement.amount_lesson]
        return date_need_pay.date or False


    @admin.display(description="Итог цены", empty_value="-")
    def result_price(self, obj):
        price = obj.abonement.price

        if obj.discount:
            return f"{price - obj.discount}р. (Скидка: {obj.discount})"
        else:
            return f"{price}р. (Скидки нет)"


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
admin.site.register(Discount)