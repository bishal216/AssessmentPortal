from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path('',views.home),
    path('ECD/',views.asECD),
    path('Dept/',views.asDepartment),
    path('Teacher/',views.asTeacher),
]