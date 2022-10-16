from django.urls import path
from .views import *

app_name = 'lancen'
urlpatterns = [
    path('', IndexPageView.as_view(), name='index' ),

    path('courses-list/', TrainingProgrammList.as_view(), name="courses_list"),
    path('course-view/<int:pk>', TrainingProgrammDetail.as_view(), name='course_view'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('stock/', StockView.as_view(), name = "stock"),

    path('free-lesson/', FreeLessonFormView.as_view(), name="free_lesson"),
    path('recall/', RecallFormView.as_view(), name="recall"),
    path('send-mail/', SendMailFormView.as_view(), name="send_mail"),
    
]