from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page,name='login_page'),
    path('student/',views.student_page,name='student_page'),
    path('teacher/',views.teacher_main,name='teacher_page'),
    path('teacher/create',views.teacher_create,name='teacher_create'),
    path('teacher/list',views.teacher_list,name='teacher_list'),
    path('teacher/detail/<int:year>/<int:rollNo>',views.teacher_detail,name='teacher_detail')
]



