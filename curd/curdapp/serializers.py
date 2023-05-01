from curdapp.models import * 
from rest_framework import serializers 

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeModel 
        fields = ['name','city','location'] 

        