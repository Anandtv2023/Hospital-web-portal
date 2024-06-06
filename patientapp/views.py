from django.shortcuts import render,redirect
from django.views.generic import CreateView,View,UpdateView,DetailView
from patientapp.forms import Registrationform,Patientform,Bookingform
from django.forms import BaseModelForm
from patientapp.models import Patient,Booking
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from userapp.models import Departmentmodel,Doctormodel
from  django.contrib.auth import logout
from django.utils.decorators import method_decorator


def Signin_requered(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper


class Registrationview(CreateView):
    template_name='patient/register.html'
    form_class=Registrationform
    model=User
    success_url=reverse_lazy('home')

class Signoutview(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('home')
    
@method_decorator(Signin_requered,name="dispatch") 
class Patientview(CreateView):
    template_name='patient/profile.html'
    form_class=Patientform
    model=Patient
    success_url=reverse_lazy('home')


    def form_valid(self,form:BaseModelForm):
        form.instance.user=self.request.user
        return super().form_valid(form)

@method_decorator(Signin_requered,name="dispatch") 
class Update_profile(UpdateView):
    template_name='patient/profile_edit.html'
    form_class=Patientform
    model=Patient
    success_url=reverse_lazy('home')

@method_decorator(Signin_requered,name="dispatch") 
class Patientdetailview(DetailView):
    template_name='patient/patient_detail.html'
    model=Patient
    context_object_name='data'

@method_decorator(Signin_requered,name="dispatch") 
class Bookingview(View):
    def get(self,request,*args,**kwargs):
        form=Bookingform()
        
        qs=Departmentmodel.objects.all()
        # q=Doctormodel.objects.all()
        return render(request,'patient/booking.html',{'form':form})
    
     
    
    def post(self,request,*args,**kwargs):
        form=Bookingform(request.POST)

        print(form)
       
        form.instance.patient=request.user
        deptc=request.POST.get('dept')
        doctc=request.POST.get('doct')
        datec=request.POST.get('date')
        print(deptc)
       
       
        data=Booking.objects.filter(dept=deptc,doct=doctc,date=datec)
        
        print(data)
        if data:
            count=0
            for i in data:
                count+=1
            form.instance.token=count+1
                
        else:
            form.instance.token=1
            
        if form.is_valid():
            form.save()
            return redirect('history')
            
                
        else: 
            print('form is not valid')
            return redirect('booking')
        

@method_decorator(Signin_requered,name="dispatch") 
class Bookinghistory(View):
    def get(self,request,*args,**kwargs):
        data=Booking.objects.filter(patient=request.user)
        return render(request,'patient/history.html',{'data':data})
    
    
@method_decorator(Signin_requered,name="dispatch") 
class Delete_booking(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Booking.objects.get(id=id).delete()
        return redirect('history')

# ===========================================

# ========================used for update the patient visiting status========================== 
@method_decorator(Signin_requered,name="dispatch")    
class BookStatusUpdate(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Booking.objects.get(id=id)
        if qs.visit==True:
            qs.visit=False
            qs.save()
        elif qs.visit==False:
            qs.visit=True
            qs.save()
        
        return redirect('book_list')

# =======================          end code       ==========================================
    
@method_decorator(Signin_requered,name="dispatch") 
class Prescibe(View):
    def get(self,request,*args,**kwargs):
        
        return render(request,'prescribe.html')
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Booking.objects.get(id=id)
        p=request.POST.get('pres')
        print(p)
        qs.prescription=p
        
        qs.save()
        
        return render(request,'prescribe.html')
    

@method_decorator(Signin_requered,name="dispatch")         
class ViewRecord(View):
        def get(self,request,*args,**kwargs):
             id=kwargs.get('pk')
             qs=Booking.objects.get(id=id)
    
             return render(request,'record.html',{'qs':qs})
        
