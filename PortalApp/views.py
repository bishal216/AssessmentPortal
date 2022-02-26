from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'PortalApp/home.html')
def asECD(request):
    return render(request,'PortalApp/ECD.html')
def asDepartment(request):
    return render(request,'PortalApp/Department.html')
def asTeacher(request):
    return render(request,'PortalApp/Teacher.html')