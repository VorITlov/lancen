from django.urls import path,re_path
from django.views.generic.base import RedirectView
from .views import *


app_name = 'profiles'
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login' ),
    path('logout/', Logout.as_view(), name='logout'),
    path('admin/', RedirectView.as_view(url = '/admin/'), name='admin'),
    path('personal-area/', PersonalArea.as_view(), name='personal_area'),

    path('edit-profile-student/<int:id>', EditStudentProfile.as_view(), name="edit_student"),

    path('change-password/', ChangePassword.as_view(template_name = "app_profiles/change_password.html"), name="change_password"),
    path('teachers-student/', ShowStudentForTeacher.as_view(), name = "teachers_student"),

]