from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def home(request):
    return render(request,'PortalApp/home.html')
def asECD(request):
    asmntStatus = AssessmentStatus.objects.all()
    return render(request,'PortalApp/ECD.html',{'asmntStatus':asmntStatus})
def asDepartment(request):
    dept = Department.objects.all()
    return render(request,'PortalApp/Department.html',{'dept':dept})
def asTeacher(request):
    return render(request,'PortalApp/Teacher.html')