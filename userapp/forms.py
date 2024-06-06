from django import forms
from userapp.models import Departmentmodel,Doctormodel

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class Departmentform(forms.ModelForm):
    class Meta:
        model=Departmentmodel
        fields=['name','d_image']

class Doctorform(forms.ModelForm):
    class Meta:
        model=Doctormodel
        fields='__all__'

