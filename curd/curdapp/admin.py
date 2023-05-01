from django.contrib import admin

from curdapp.models import * 
@admin.register(CollegeModel)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','location']

