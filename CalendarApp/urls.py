from django.urls import path
from CalendarApp import views

urlpatterns = [
    path('', views.calendar, name='calendar'),
]
