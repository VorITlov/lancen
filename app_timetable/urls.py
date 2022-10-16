from django.urls import include, path
from .views import CreateTimetablesFormView

app_name = 'timetable'

urlpatterns = [
    path('create_timitable/', CreateTimetablesFormView.as_view(), name='create_timetable'),
]
