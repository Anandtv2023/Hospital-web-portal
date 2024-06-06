"""
URL configuration for HOST project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from userapp.views import Signinview,Signoutview,Adddepartment,Departmentremove,Adddoctor,Doctorremove,Homepageview,Update_department,Update_doctor,Doctorbookinglist,About

urlpatterns = [
    
    
    
    # path('',Deptview.as_view(),name='home'),
    path('',Homepageview.as_view(),name='home'),
    
    path('signin/',Signinview.as_view(),name='login'),
    path('signout/',Signoutview.as_view(),name='logout'),

    path('adddept/',Adddepartment.as_view(),name='dept'),
    path('deptdelete/<int:pk>',Departmentremove.as_view(),name='del_dept'),
    path('update_dept/<int:pk>/',Update_department.as_view(),name='update_d'),

    path('adddoctor/',Adddoctor.as_view(),name='adddoctor'),
    path('docterdelete/<int:pk>',Doctorremove.as_view(),name='del_doc'),
    path('update_doct/<int:pk>/',Update_doctor.as_view(),name='update_doc'),

    path('doctorbookinglist/',Doctorbookinglist.as_view(),name='book_list'),
     path('About/',About.as_view(),name='about')

]
