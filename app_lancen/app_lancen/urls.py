from django.urls import path
from .views import *

app_name = 'lancen'
urlpatterns = [
    path('', IndexPageView.as_view(), name='index' ),

    path('courses-list/', TrainingProgrammList.as_view(), name="courses_list"),
    path('course-view/<int:pk>', TrainingProgrammDetail.as_view(), name='course_view'),
    path('contact/', ContactView.as_view(), name='contact'),

    path('free-lesson/', FreeLessonFormView.as_view(), name="free_lesson")
]