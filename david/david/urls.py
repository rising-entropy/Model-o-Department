
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing_page,name='login_page'),
]
