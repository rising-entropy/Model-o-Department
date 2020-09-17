from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page,name='login_page'),
    path('student/<int:year>/<int:rollNo>',views.student_page,name='student_page'),
    path('teacher/',views.student_page,name='teacher_page'),
    path('teacher/create',views.student_page,name='teacher_create'),
    path('teacher/list',views.student_page,name='teacher_list'),
    path('teacher/detail/<int:year>/<int:rollNo>',views.student_page,name='teacher_detail')
]



