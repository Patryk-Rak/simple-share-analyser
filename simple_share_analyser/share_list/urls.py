from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('share_list/', views.share_list, name="share_list"),
    path('share_form/', views.share_form, name="share_form"),
    path('share_list/<id>/delete', views.share_delete, name="share_delete"),

]
