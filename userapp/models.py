from django.db import models

# Create your models here.

class Departmentmodel(models.Model):
    name=models.CharField(max_length=20,unique=True)
    d_image=models.ImageField(upload_to='images',null=True)

    def __str__(self):
        return self.name


class Doctormodel(models.Model):
    department=models.ForeignKey(Departmentmodel,on_delete=models.CASCADE)
    doctor=models.CharField(max_length=25)

    def __str__(self):
        return self.doctor