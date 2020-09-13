from django.contrib import admin
from django.urls import path,include
import david.views as views

urlpatterns = [
    path('',views.landingPage),
    path('admin/', admin.site.urls),
]
