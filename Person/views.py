from django.shortcuts import render
from django.views.generic import CreateView,DetailView,DeleteView,ListView,UpdateView
from django.views import View
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import person
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class Allperson(ListView):
    model=person
    template_name='indexperson.html'

class Detailperson(DetailView):
    model=person   
    template_name='indexdetail.html'

class Createperson(CreateView):
    model=person
    template_name='indexcreate.html'
    fields=['name','family','age','national_id']

class Updateperson(UpdateView):
    model=person
    template_name='indexupdate.html'
    fields=['name','family','age','national_id']

class Deleteperson(DeleteView):
    model=person
    success_url=reverse_lazy('all')
    template_name='indexdelete.html'


class Createuser(View):
    def get(self,request):
        form=UserCreationForm()
        context={'Form':form}
        return render(request,'usercreate.html',context)    
    def post(self,request):
        form=UserCreationForm(request.POST)
        if not form.is_valid():
            form=UserCreationForm()
            context={'Form':form}
            return render(request,'usercreate.html',context)
        else:
            form.save()
            return HttpResponse('Created successfully')
        
class Authuser(View):
    def get(self,request):
        form=AuthenticationForm()
        context={'Form':form}
        return render(request,'authuser.html',context)
    def post(self,request):
        form=AuthenticationForm(data=request.POST)
        if not form.is_valid():
            form=AuthenticationForm()
            context={'Form':form}
            return render(request,'authuser.html',context)
        else:
            useruser=form.get_user()
            login(request,useruser)
            return HttpResponse('Auth Auth !!!!')
        
class LOGOUT(View):
    def get(self,request):
        logout(request)
        return HttpResponse("this is Logout ^_^")
    def post(self,requset):
        return HttpResponse("Nothing.")
    


class testapicbv(APIView):
    def get(self,request):
        x=request.query_params['name']
        return Response({'status':x})
    def post(self,request):
        x=request.data['name']
        return Response({'status':x})

    

