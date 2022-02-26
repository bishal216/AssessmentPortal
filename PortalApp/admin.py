from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Section)
admin.site.register(Teacher)
admin.site.register(ECD)
admin.site.register(Department)
admin.site.register(AssessmentStatus)
