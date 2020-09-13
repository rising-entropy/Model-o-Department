
from django.contrib import admin
from . import views
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing_page,name='login_page'),
]
