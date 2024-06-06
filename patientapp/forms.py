from django import forms
from django.contrib.auth.models import User
from patientapp.models import Patient,Booking
from django.contrib.auth.forms import UserCreationForm


class Registrationform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','password1','password2','email']



class Patientform(forms.ModelForm):
    class Meta:
        model=Patient
        exclude=('user',)
        fields='__all__'

class Bookingform(forms.ModelForm):
    class Meta:
        model=Booking
        exclude=('token','patient','visit','prescription')
        fields='__all__'

