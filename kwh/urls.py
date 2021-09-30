from django.contrib import admin
from django.urls import path, include
from .views import addFemsTransData
from . import views
urlpatterns = [
    path('temp/monitor/', addFemsTransData.as_view()),
    path('temp/list/', views.fems_datalist),
]
