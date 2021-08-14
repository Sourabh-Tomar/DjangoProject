from django.urls import path
from . import views


urlpatterns = [
    path('',views.learn_django, name='learn'),
    path('students/',views.studentwala,name='student')
]