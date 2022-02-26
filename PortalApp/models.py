
from django.db import models

#ECD
class ECD(models.Model):
    name= models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
#Department
class Department(models.Model):
    name= models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
#ECD
class Teacher(models.Model):
    name= models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
#Section
class Section(models.Model):
    year = models.CharField(max_length=3,null=True)
    dept= models.CharField(max_length=3,null=True)
    sec = models.CharField(max_length=1,null=True)
    
    def __str__(self):
        return str(self.year)+self.dept+self.sec

#AssessmentStatus
class AssessmentStatus(models.Model):
    STATUS = (
        ('Unsubmitted','Unsubmitted'),
        ('Submitted','Submitted'),
        ('Approved','Approved'),
        ('Rejected','Rejected'),
    )
    Submitter = models.ForeignKey(Teacher,null=True, on_delete=models.DO_NOTHING)
    Section = models.ForeignKey(Section,null=True,on_delete=models.DO_NOTHING)
    Subject = models.CharField(max_length=100,null=True)
    Status = models.CharField(max_length=100,choices=STATUS)
    FullMarks = models.IntegerField(null=True)
    
    def __str__(self):
        return self.Subject+self.Section.__str__()