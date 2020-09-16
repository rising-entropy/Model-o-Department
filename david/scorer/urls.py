from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page,name='login_page'),
    path('student/',views.student_page,name='student_page'),
]



