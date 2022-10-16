from django.urls import path
from .views import *


app_name = 'journal'
urlpatterns = [
    path('journals/', TeachersJournalList.as_view(), name='journals' ),
    path('view-journal/<int:group>/<int:year>/<int:month>/', JournalMonthView.as_view(month_format='%m'), name='view-journal'),


    path('delete-attendance/<int:stud_id>/<int:timetable_id>', delete_attendance, name="delete_attendance"),
    path('expose-attendance/<int:stud_id>/<int:timetable_id>', expose_attendance, name="expose_attendance"),


    path('expose-mark/<int:student>/<int:lesson_date>/<str:date>', ExposeMark.as_view(), name =  'expose_mark' ),
    path('update-mark/<int:id_mark>/<int:id_group>/<int:year>/<str:month>/', UpdateMark.as_view(), name =  'update_mark' ),
    path('delete-mark/<int:id_mark>', delete_mark , name="delete_mark"),


    path('student_marks/', StudentMarkView.as_view(), name="student_marks"),
]