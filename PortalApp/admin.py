# import
from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

#ModelAdmin Classes
class _Student(admin.ModelAdmin):
    #exclude = ('StdList', ) #Exclude from Input field
    list_display = ['Batch','Dept','Name','Roll'] #Display given fields
    search_fields = ['Batch','Dept','Name']

# class _Asmnt(admin.ModelAdmin):
#     exclude =('upload',)

#Register Model
admin.site.register(Section)
admin.site.register(Teacher)
admin.site.register(ECD)
admin.site.register(Department)
admin.site.register(AssessmentStatus)
admin.site.register(StudentData,_Student)
#Unregister Model
admin.site.unregister(Group)
#Changing adimin site
admin.site.site_header = "Admin Portal for Internal Assessment Submission"


