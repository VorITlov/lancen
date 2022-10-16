
from django.urls import path
from .views import *
from django.views.generic.base import RedirectView
from django.urls.base import reverse

from datetime import datetime
import datetime as dt

current_datetime = datetime.now()
week = dt.date(current_datetime.year, current_datetime.month, current_datetime.day).strftime("%V")

app_name = "homework"
urlpatterns = [
    path('expose-homework/',ExposeHomework.as_view(), name="expose_homework"),
    path('update-homework/<int:id>', UpdateHomework.as_view(), name = "update_homework"),
    path('delete-homework/<int:id>', DeleteHomework.as_view(), name = "delete_homework"),
    path('homework-list/', HomeworkList.as_view(), name="homework_list"),

    path('homework-list-student/<int:year>/<int:week>/', HomeworkListStudent.as_view(), name = "homework_list_student"),


    path('delete-file/<int:id_file>/<int:id_hw>', delete_file, name="delete_file" ),
    # path('go-to-stud-hw/', RedirectView.as_view(url = reverse('homework:homework_list_student', args=[current_datetime.year,week ])), name = "go_to_stud_hw"),
    path('go-to-stud-hw/', RedirectView.as_view(url = f"/homework/homework-list-student/{current_datetime.year}/{week}/"), name = "go_to_stud_hw"),

]