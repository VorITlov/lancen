from django.urls import path
from .views import *

app_name = 'abonements'
urlpatterns = [

    path('abonement-detail/<int:pk>/<int:id_course>', AbonementDeatil.as_view(), name = "abonement_detail" ),
    path('student-abonements/', StudentAbonementsView.as_view(), name="student_abonements"),
    path('student-payment-lessons/', StudentPaymentLesson.as_view(), name="student_payment_lessons"),


    
]
