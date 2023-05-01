from django.shortcuts import render

from curdapp.models import * 
from curdapp.serializers import * 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 
@api_view(['POST'])
def college_create(request):
    serializer = CollegeSerializer(data= request.data) 
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'serializer':serializer.data,'status':status.HTTP_201_CREATED}) 


@api_view(['GET'])
def college_get(request):
    clg = CollegeModel.objects.all()
    serializer = CollegeSerializer(clg,many = True) 
    return Response({'get_data':serializer.data,'status':status.HTTP_200_OK}) 


@api_view(['PUT'])
def college_put(request,pk):
    clg = CollegeModel.objects.get(id = pk)
    serializer = CollegeSerializer(clg,data=request.data) 
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'put_data':serializer.data,'status':status.HTTP_200_OK})

@api_view(['PATCH'])
def college_patch(request,pk):
    clg = CollegeModel.objects.get(id= pk)
    serializer = CollegeSerializer(clg,data=request.data,partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'patch':serializer.data,'status':status.HTTP_200_OK}) 


@api_view(['DELETE'])
def college_delete(request,pk):
    clg = CollegeModel.objects.get(id=pk)
    clg.delete()
    return Response({'delete':'data has deleted successfully '}) 
