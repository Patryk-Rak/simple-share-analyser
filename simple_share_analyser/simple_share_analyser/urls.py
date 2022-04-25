from django.contrib import admin
from django.urls import path, include

from share_list import views

app_name = 'main_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('share_list.urls')),
]
