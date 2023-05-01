
from django.contrib import admin
from django.urls import path
from curdapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',views.college_create),
    path('get/',views.college_get),
    path('put/<int:pk>',views.college_put),
    path('patch/<int:pk>',views.college_patch),
    path('delete/<int:pk>',views.college_delete),
]
