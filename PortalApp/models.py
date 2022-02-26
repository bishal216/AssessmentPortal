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
    year = models.IntegerField(null=True)
    dept= models.CharField(max_length=200,null=True)
    sec = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.year+self.dept+self.sec