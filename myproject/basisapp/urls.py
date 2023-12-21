from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    #path('lec1_1app/', lec1_1app.views),
    ]