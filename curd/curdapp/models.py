from django.db import models

class CollegeModel(models.Model):
    name = models.CharField(max_length=18)
    city = models.CharField(max_length=25)
    location = models.CharField(max_length=23)

    def __str__(self):
        return self.name 
    
class Student(models.Model):
    sname = models.CharField(max_length=50,null = True, blank=True)
    # sid = models.IntegerField(_(""))