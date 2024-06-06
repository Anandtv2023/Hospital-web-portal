from django.shortcuts import render,redirect
from django.views.generic import View,FormView,CreateView,ListView,TemplateView,UpdateView
from userapp.forms import Loginform,Departmentform,Doctorform
from userapp.models import Departmentmodel,Doctormodel
from patientapp.models import Booking
from  django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


def Signin_requered(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect('login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper




# ================================================================

class Homepageview(View):
    def get(self,request,*args,**kwargs):
        data=Departmentmodel.objects.all()
        return render(request,'index.html',{'data':data})
    

    
# class Deptview(ListView):
#     template_name='index.html'
#     form_class=Departmentform
#     model=Departmentmodel
#     context_object_name='data'
    
class Signinview(FormView):
    template_name='login.html'
    form_class=Loginform

    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                if request.user.is_superuser:
                    print('success')
                    return redirect('home')
                else:
                    return redirect('home')
            else:
                
                return render(request,'login.html',{'form':form})
            

class Signoutview(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('home')
    

# ==============================================================
    

class Adddepartment(CreateView,ListView):
    template_name='dept.html'
    form_class=Departmentform
    model=Departmentmodel
    success_url=reverse_lazy('dept')
    context_object_name='data'

@method_decorator(Signin_requered,name="dispatch") 
class Departmentremove(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Departmentmodel.objects.get(id=id).delete()
        return redirect('dept')
    

# class Update_department(UpdateView):
#     template_name='updatedept.html'
#     form_class=Departmentform
#     model=Departmentmodel
#     success_url=reverse_lazy('dept')
#     context_object_name='data'
    
@method_decorator(Signin_requered,name="dispatch") 
class Update_department(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Departmentmodel.objects.get(id=id)
        form=Departmentform(instance=obj)
        return render(request,'updatedept.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Departmentmodel.objects.get(id=id)
        form=Departmentform(request.POST,files=request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('dept')
        else:
            print('not valid')

# ===============================================================
    


class Adddoctor(CreateView,ListView):
    template_name='doctor.html'
    form_class=Doctorform
    model=Doctormodel
    success_url=reverse_lazy('adddoctor')
    context_object_name='data'
    

@method_decorator(Signin_requered,name="dispatch") 
class Doctorremove(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Doctormodel.objects.get(id=id).delete()
        return redirect('adddoctor')
    

@method_decorator(Signin_requered,name="dispatch") 
class Update_doctor(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Doctormodel.objects.get(id=id)
        form=Doctorform(instance=obj)
        return render(request,'updatedoct.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Doctormodel.objects.get(id=id)
        form=Doctorform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('adddoctor')
        else:
            print('not valid')



# ===================================================================
            

# ==================doctors booking list=============================
@method_decorator(Signin_requered,name="dispatch") 
class Doctorbookinglist(View):
    def get(self,request,*args,**kwargs):
        return render(request,'dhistory.html')
    

    def post(self,request,*args,**kwargs):
        ddid=request.POST.get('did')
        bbdate=request.POST.get('bdate')
        data=Booking.objects.filter(doct=ddid,date=bbdate)
        return render(request,'dhistory.html',{'data':data})




class About(View):
    def get(self,request,*args,**kwargs):
        return render(request,'about.html')

    


    