from django.db import models
from django.contrib.auth.models import User
from userapp.models import Departmentmodel,Doctormodel

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=300)
    age=models.PositiveIntegerField()
    contact=models.CharField(max_length=30)
    email=models.EmailField(max_length=200)
    options=(
        ('male','male'),('female','female'),('others','others')
    )
    gender=models.CharField(max_length=20,choices=options,default='male')
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,related_name='profile')#oru patientinu oru profile matrame create cheyyavu athinanu ithu
    # related_name=profile kodukkkunnath aa table ne represent cheyynanau
    def __str__(self):
        return self.name
    

class Booking(models.Model):
    patient=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    dept=models.ForeignKey(Departmentmodel,on_delete=models.DO_NOTHING)
    doct=models.ForeignKey(Doctormodel,on_delete=models.DO_NOTHING)
    date=models.DateField()
    token=models.PositiveIntegerField()
    visit=models.BooleanField(default=False,null=True)
    prescription=models.TextField(max_length=1000,null=True)
    